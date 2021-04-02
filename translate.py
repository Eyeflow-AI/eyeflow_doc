import os
import re
import datetime
import json
import hashlib

from google.cloud import translate_v2 as translate
# ---------------------------------------------------------------------------------------------------------------------------------

class TextTranslate():

    def __init__(self, lang) -> None:
        self.text_ids = {}
        self.text_id = None
        self.source_language = lang
        self.load_proj()


    def load_proj(self):
        proj_filename = os.path.join(os.path.dirname(__file__), "text_translate.json")
        if os.path.exists(proj_filename):
            with open(proj_filename, 'r', encoding='utf-8') as fp:
                self.text_ids = json.load(fp)


    def save_proj(self):
        with open(os.path.join(os.path.dirname(__file__), "text_translate.json"), 'w', encoding='utf-8') as fp:
            json.dump(self.text_ids, fp, indent=2, ensure_ascii=False, default=str)


    @staticmethod
    def get_text_hash(text):
        return str(int(hashlib.sha512(text.encode('utf-8')).hexdigest()[:16], 16))


    def upsert_text(self, text):
        text_id = self.get_text_hash(text)

        if text_id not in self.text_ids:
            self.text_ids[text_id] = {
                "text": text,
                "source_language": self.source_language
            }
        else:
            self.text_ids[text_id]["text"] = text


    def add_text(self, text, update=False):
        if update:
            del self.text_ids[self.text_id]

        if len(text) < 1:
            return

        re_links = re.compile(r'!*\[(.*?)\]\(.*?\)\S*')
        search = re_links.search(text)
        while search:
            if len(search.group(1)):
                self.upsert_text(search.group(1))

            re_desc = re.compile(r'\((.*?)\s+"(.*?)"\)')
            search_desc = re_desc.search(text)
            if search_desc and len(search_desc.group(2)):
                self.upsert_text(search_desc.group(2))

            if search.group(0) == text:
                return

            if search.group(0).startswith('!') or search.group(0).endswith(':'):
                text = (text[0:search.regs[0][0]] + text[search.regs[0][1]:]).lstrip()
            else:
                if len(text[0:search.regs[0][0]]):
                    self.upsert_text(text[0:search.regs[0][0]])
                text = text[search.regs[0][1]:].lstrip()

            search = re_links.search(text)

        if len(text) < 1:
            return

        re_links = re.compile(r'```.*```')
        search = re_links.search(text)
        while search:
            text = (text[0:search.regs[0][0]] + text[search.regs[0][1]:]).lstrip()
            search = re_links.search(text)

        if len(text) < 1:
            return

        self.text_id = self.get_text_hash(text)
        self.upsert_text(text)


    def get_translated_text(self, text, lang):
        text_id = self.get_text_hash(text)
        if text_id not in self.text_ids:
            return None

        return self.text_ids[text_id][lang]["text"]


    def translate_text(self, target):
        """Translates text into the target language.

        Target must be an ISO 639-1 language code.
        See https://g.co/cloud/translate/v2/translate-reference#supported_languages
        """

        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/alexsobral/.ssh/gcloud-service-account.json'
        translate_client = translate.Client()

        for text_id in self.text_ids:
            if target not in self.text_ids[text_id]:
                result = translate_client.translate(
                    self.text_ids[text_id]["text"],
                    source_language=self.source_language,
                    target_language=target
                )

                self.text_ids[text_id][target] = {
                    "text": result["translatedText"],
                    "date": datetime.datetime.now(),
                    "approved": False
                }

# ---------------------------------------------------------------------------------------------------------------------------------

def flatten_text(file_content):
    idx = 0
    state = None
    while idx < len(file_content) - 1:
        line = file_content[idx].lstrip().replace('\n', '')
        if line == "---":
            if state is None:
                state = "header"
                idx += 1
                continue
            elif state == "header":
                state = "body"
                idx += 1
                continue

        if state == "header":
            re_links = re.compile(r'^description:\s*>*"*(.*)"*')
            search = re_links.search(line)
            if search:
                text = f'description: {search.group(1)}'
                next_line = file_content[idx + 1].replace('\n', '')
                while next_line.startswith(' '):
                    text += next_line
                    del file_content[idx + 1]
                    if idx < len(file_content) - 1:
                        next_line = file_content[idx + 1].replace('\n', '').lstrip()

                file_content[idx] = text + '\n'

            idx += 1
            continue

        if len(line) < 1 or line.startswith('#') or line.startswith('|') or line.startswith('{'):
            state = "body"
            idx += 1
            continue

        if state == "code":
            if line.startswith('```'):
                state = "body"

            idx += 1
            continue

        if line.startswith('```'):
            state = "code"
            idx += 1
            continue

        re_search = re.compile(r'^(\s*[\-*\d]+\.*\s+)(.*)')
        search = re_search.search(line)
        if search:
        # if line.startswith('- ') or line.startswith('* '):
            text = file_content[idx].replace('\n', '')
            next_line = file_content[idx + 1].replace('\n', '').lstrip()
            next_search = re_search.search(next_line)
            while len(next_line) > 0 and not next_search and idx < len(file_content) - 1:
                text += ' ' + next_line
                del file_content[idx + 1]
                if idx < len(file_content) - 1:
                    next_line = file_content[idx + 1].replace('\n', '').lstrip()

            file_content[idx] = text + '\n'
            idx += 1
            continue

        if line.startswith('> '):
            text = line
            next_line = file_content[idx + 1].replace('\n', '').lstrip()
            while len(next_line) > 0 and next_line[0] == '>' and idx < len(file_content) - 1:
                text += ' ' + next_line[1:].lstrip()
                del file_content[idx + 1]
                if idx < len(file_content) - 1:
                    next_line = file_content[idx + 1].replace('\n', '').lstrip()

            file_content[idx] = text + '\n'
            idx += 1
            continue

        if state == "body":
            text = line
            next_line = file_content[idx + 1].replace('\n', '').lstrip()
            # next_search = re_search.search(next_line)
            while len(next_line) > 0 and next_line[0] not in ['-', '*', '#', '>', '1', '{'] and idx < len(file_content) - 1:
                text += ' ' + next_line
                del file_content[idx + 1]
                if idx < len(file_content) - 1:
                    next_line = file_content[idx + 1].replace('\n', '').lstrip()

            file_content[idx] = text + '\n'
            idx += 1
            continue

    return file_content
# ---------------------------------------------------------------------------------------------------------------------------------

def extract_text(file_content, text_trans):
    state = None
    for line in file_content:
        line = line.lstrip().replace('\n', '')
        if line == "---":
            if state is None:
                state = "header"
                continue
            elif state == "header":
                state = "body"
                continue

        if state == "header":
            re_links = re.compile(r'^title:\s*"(.*?)"')
            search = re_links.search(line)
            if search:
                text_trans.add_text(search.group(1))
                continue

            re_links = re.compile(r'^linkTitle:\s*"(.*?)"')
            search = re_links.search(line)
            if search:
                text_trans.add_text(search.group(1))
                continue

            re_links = re.compile(r'^description:\s*>*"*(.*)"*')
            search = re_links.search(line)
            if search:
                text_trans.add_text(search.group(1))
                continue

            continue

        if len(line) < 1:
            state = "body"
            continue

        if state == "code":
            if line.startswith('```'):
                state = "body"

            continue

        if line.startswith('```'):
            state = "code"
            continue

        re_links = re.compile(r'<!--(.*?)-->')
        search = re_links.search(line)
        if search:
            line = (line[0:search.regs[0][0]] + line[search.regs[0][1]:]).lstrip()
            if len(line) < 1:
                continue

        re_links = re.compile(r'\{\{< /?note >\}\}')
        search = re_links.search(line)
        while search:
            line = (line[0:search.regs[0][0]] + line[search.regs[0][1]:]).lstrip()
            search = re_links.search(line)
        if len(line) < 1:
            continue

        re_links = re.compile(r'\{\{< /?tooltip >\}\}')
        search = re_links.search(line)
        while search:
            line = (line[0:search.regs[0][0]] + line[search.regs[0][1]:]).lstrip()
            search = re_links.search(line)
        if len(line) < 1:
            continue

        if line[0] in ['!', '[', '|']:
            state = "body"
            continue

        if line[0] == '#':
            text = line[line.find(' ') + 1:].lstrip()
            text_trans.add_text(text)
            continue

        if line.startswith('- ') or line.startswith('* ') or line.startswith('> '):
            text = line[line.find(' ') + 1:].lstrip()
            text_trans.add_text(text)
            continue

        if state == "body":
            text = line
            text_trans.add_text(text)
            continue

        raise Exception(f"Unknow state: {state}")
# ---------------------------------------------------------------------------------------------------------------------------------

def extract_ids(source_language, text_trans):
    source_path = os.path.join(os.path.dirname(__file__), f'content/{source_language}/docs')
    for root, dirs, files in os.walk(source_path):
        for filename in files:
            if filename.endswith('.md'):
                print(f'Extracting file: {os.path.join(root, filename)}')

                with open(os.path.join(root, filename), 'r', encoding='utf-8') as fp:
                    file_text = fp.readlines()

                flatten_text(file_text)
                extract_text(file_text, text_trans)
# ---------------------------------------------------------------------------------------------------------------------------------


def translate_text(file_content, target_language, text_trans):
    dest_content = []
    state = None
    for input_line in file_content:
        line = input_line.lstrip().replace('\n', '')
        if line == "---":
            if state is None:
                state = "header"
                dest_content.append(input_line)
                continue
            elif state == "header":
                dest_content.append(input_line)
                state = "body"
                continue

        if state == "header":
            re_links = re.compile(r'^title:\s*"(.*?)"')
            search = re_links.search(line)
            if search:
                trans_text = text_trans.get_translated_text(search.group(1), target_language)
                dest_content.append(f'title: "{trans_text}"\n')
                continue

            re_links = re.compile(r'^linkTitle:\s*"(.*?)"')
            search = re_links.search(line)
            if search:
                trans_text = text_trans.get_translated_text(search.group(1), target_language)
                dest_content.append(f'linkTitle: "{trans_text}"\n')
                continue

            re_links = re.compile(r'^description:\s*"*(.*)"*')
            search = re_links.search(line)
            if search:
                trans_text = text_trans.get_translated_text(search.group(1), target_language)
                dest_content.append(f"description: >\n")
                dest_content.append(f" {trans_text}\n")
                continue

            dest_content.append(input_line)
            continue

        if len(line) < 1:
            state = "body"
            dest_content.append('\n')
            continue

        re_links = re.compile(r'<!--(.*?)-->')
        search = re_links.search(line)
        while search:
            dest_content.append(f'{line[search.regs[0][0]:search.regs[0][1]]}\n')
            line = (line[0:search.regs[0][0]] + line[search.regs[0][1]:]).lstrip()
            search = re_links.search(line)

        if len(line) < 1:
            continue

        re_links = re.compile(r'\{\{< note >\}\}')
        search = re_links.search(line)
        if search:
            if search.regs[0][0] != 0:
                raise Exception("Note not first position")

            dest_content.append(f'{line[search.regs[0][0]:search.regs[0][1]]}\n')
            line = (line[0:search.regs[0][0]] + line[search.regs[0][1]:]).lstrip()

        re_links = re.compile(r'\{\{< /note >\}\}')
        search = re_links.search(line)
        if search:
            text = line[0:search.regs[0][0]]
            trans_text = text_trans.get_translated_text(text, target_language)
            if trans_text:
                dest_content.append(f'{trans_text}\n')
            dest_content.append(f'{line[search.regs[0][0]:search.regs[0][1]]}\n')

            line = (line[search.regs[0][1]:]).lstrip()
            if line:
                raise Exception("End Note not last position")

        re_links = re.compile(r'\{\{< tooltip >\}\}')
        search = re_links.search(line)
        if search:
            if search.regs[0][0] != 0:
                raise Exception("Note not first position")

            dest_content.append(f'{line[search.regs[0][0]:search.regs[0][1]]}\n')
            line = (line[0:search.regs[0][0]] + line[search.regs[0][1]:]).lstrip()

        re_links = re.compile(r'\{\{< /tooltip >\}\}')
        search = re_links.search(line)
        if search:
            text = line[0:search.regs[0][0]]
            trans_text = text_trans.get_translated_text(text, target_language)
            if trans_text:
                dest_content.append(f'{trans_text}\n')
            dest_content.append(f'{line[search.regs[0][0]:search.regs[0][1]]}\n')

            line = (line[search.regs[0][1]:]).lstrip()
            if line:
                raise Exception("End Note not last position")


        if len(line) < 1:
            continue

        if line[0] in ['|']:
            dest_content.append(input_line)
            state = "body"
            continue

        if state == "code":
            dest_content.append(input_line)
            if line.startswith('```'):
                state = "body"
            continue

        if line.startswith('```'):
            dest_content.append(input_line)
            state = "code"
            continue

        re_search = re.compile(r'^(\s*[\-*>#]+\s+)(.*)')
        search = re_search.search(input_line)
        if search:
            dest_content.append(search.group(1))
            line = search.group(2)
            state = "continue"

        re_links = re.compile(r'(!*)\[(.*?)\]\((.*?)\)')
        search = re_links.search(line)
        links = []
        while search:
            alt_text = search.group(2)
            if len(alt_text):
                trans_text = text_trans.get_translated_text(alt_text, target_language)
                if trans_text:
                    alt_text = trans_text

            desc = ''
            re_desc = re.compile(r'\((.*)\s"(.*)"\)')
            search_desc = re_desc.search(search.group(3))
            if search_desc and len(search_desc.group(2)):
                desc = search_desc.group(2)
                trans_text = text_trans.get_translated_text(desc, target_language)
                if trans_text:
                    desc = trans_text

                links.append(search.group(1) + '[' + alt_text + '](' + search_desc.group(1) + ' "' + desc + '")')
            else:
                links.append(search.group(1) + '[' + alt_text + '](' + search.group(3) + ')')

            if search.group(0).startswith('!') or search.group(0).endswith(':'):
                line = (line[0:search.regs[0][0]] + line[search.regs[0][1]:]).lstrip()
                search = re_links.search(line, search.regs[0][1])
            else:
                if len(line[0:search.regs[0][0]]):
                    trans_text = text_trans.get_translated_text(line[0:search.regs[0][0]], target_language)
                    if trans_text:
                        if state == 'body':
                            dest_content.append(f'{trans_text} ')
                            state = "continue"
                        elif state == 'continue':
                            dest_content[-1] += trans_text

                line = links[-1] + ' ' + line[search.regs[0][1]:].lstrip()
                search = re_links.search(line, len(links[-1]))

        while links:
            if state == "body":
                dest_content.append(f'{links.pop()}\n')
            elif state == 'continue':
                dest_content[-1] += links.pop()

        if len(line) < 1:
            continue

        if state == "body":
            text = line
            trans_text = text_trans.get_translated_text(text, target_language)
            if trans_text:
                dest_content.append(f'{trans_text}\n')
            continue
        elif state == 'continue':
            text = line
            trans_text = text_trans.get_translated_text(text, target_language)
            if trans_text:
                dest_content[-1] += trans_text

            dest_content[-1] += '\n'

    re_bold = re.compile(r'\*\s(.*?)\s\*')
    for idx, lin in enumerate(dest_content):
        dest_content[idx] = re_bold.sub(r'*\1*', lin)
    return dest_content
# ---------------------------------------------------------------------------------------------------------------------------------

def translate_lang(source_language, target_language, text_trans):
    source_path = os.path.join(os.path.dirname(__file__), f'content/{source_language}/docs')
    target_path = os.path.join(os.path.dirname(__file__), f'content/{target_language}/docs')

    # with open(os.path.join(os.path.join(os.path.dirname(__file__), f'content/{source_language}/docs/Concepts/flow.md')), 'r', encoding='utf-8') as fp:
    #     file_text = fp.readlines()

    # flatten_text(file_text)
    # dest_text = translate_text(file_text, target_language, text_trans)

    # with open(os.path.join(os.path.join(os.path.dirname(__file__), f'content/{target_language}/docs/Overview/_index.md')), 'w', encoding='utf-8') as fp:
        # fp.writelines(dest_text)


    for root, dirs, files in os.walk(source_path):
        for filename in files:
            if filename.endswith('.md'):
                print(f'Converting file: {os.path.join(root, filename)}')

                with open(os.path.join(root, filename), 'r', encoding='utf-8') as fp:
                    file_text = fp.readlines()

                flatten_text(file_text)
                dest_text = translate_text(file_text, target_language, text_trans)

                dest_path = root.replace(source_path, target_path)
                with open(os.path.join(dest_path, filename), 'w', encoding='utf-8') as fp:
                    fp.writelines(dest_text)
# ---------------------------------------------------------------------------------------------------------------------------------

text_trans = TextTranslate('pt-br')
extract_ids('pt', text_trans)
text_trans.translate_text('en')
text_trans.save_proj()

translate_lang('pt', 'en', text_trans)
