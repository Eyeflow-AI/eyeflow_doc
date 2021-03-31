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

        re_links = re.compile(r'!*\[(.*)\]\((.*)\s*"*(.*)"*\)\S*')
        search = re_links.search(text)
        if search:
            if len(search.group(1)):
                self.upsert_text(search.group(1))

            if len(search.group(3)):
                self.upsert_text(search.group(3))

            text = (text[0:search.regs[0][0]] + text[search.regs[0][1]:]).lstrip()
            if len(text) < 1:
                return

        re_links = re.compile(r'```.*```')
        search = re_links.search(text)
        if search:
            text = (text[0:search.regs[0][0]] + text[search.regs[0][1]:]).lstrip()
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


def extract_text(file_content, text_trans):
    state = None
    for line in file_content:
        line = line.lstrip().replace('\n', '')
        if line == "---":
            if state is None:
                state = "header"
                description = None
                continue
            elif state == "header":
                if description:
                    text_trans.add_text(description)

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

            re_links = re.compile(r'^description:\s*>*"(.*?)"')
            search = re_links.search(line)
            if search:
                description = search.group(1)
                continue

            if description is not None:
                description += line
            continue

        if len(line) < 1:
            state = "body"
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

        if line[0] in ['!', '[', '|']:
            state = "body"
            continue

        if line[0] == '```':
            if state != "code":
                state = "code"
                continue
            else:
                state = "body"
                continue

        if line[0] == '#':
            text = line[line.find(' ') + 1:].lstrip()
            text_trans.add_text(text)
            continue

        if line.startswith('- ') or line.startswith('* '):
            text = line[line.find(' ') + 1:].lstrip()
            text_trans.add_text(text)
            state = "text"
            continue

        if line.startswith('> '):
            line = line[line.find(' ') + 1:].lstrip()

        if state == "body":
            text = line
            text_trans.add_text(text)
            state = "text"
            continue

        if state == "text":
            text += ' ' + line
            text_trans.add_text(text, True)
            state = "text"
            continue

# ---------------------------------------------------------------------------------------------------------------------------------

def extract_ids(base_path, text_trans):
    for root, dirs, files in os.walk(base_path):
        for filename in files:
            if filename.endswith('.md'):
                print(f'Converting file: {os.path.join(root, filename)}')

                with open(os.path.join(root, filename), 'r', encoding='utf-8') as fp:
                    file_text = fp.readlines()

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
                description = None
                dest_content.append(input_line)
                continue
            elif state == "header":
                if description:
                    trans_text = text_trans.get_translated_text(description, target_language)
                    dest_content.append(f"description: >\n {trans_text}\n")

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

            re_links = re.compile(r'^description:\s*>*"(.*?)"')
            search = re_links.search(line)
            if search:
                description = search.group(1)
                continue

            if description is not None:
                description += line
            continue

        if len(line) < 1:
            state = "body"
            dest_content.append('\n')
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
            dest_content.append('line[search.regs[0][0]:search.regs[0][1]]\n')
            line = (line[0:search.regs[0][0]] + line[search.regs[0][1]:]).lstrip()
            search = re_links.search(line)
        if len(line) < 1:
            continue

        if line[0] in ['!', '[', '|']:
            dest_content.append(input_line)
            state = "body"
            continue

        if state == "code":
            dest_content.append(input_line)
            if line[0] == '```':
                state = "body"
                continue

        if line[0] == '```':
            dest_content.append(input_line)
            if state != "code":
                state = "code"
                continue
            else:
                state = "body"
                continue

        if line[0] == '#':
            idx = line.find(' ') + 1
            text = line[idx:].lstrip()

            trans_text = text_trans.get_translated_text(text, target_language)
            dest_content.append(f'{line[:idx]}{trans_text}\n')

            continue

        if line.startswith('- ') or line.startswith('* '):
            idx = line.find(' ') + 1
            text = line[idx:].lstrip()

            trans_text = text_trans.get_translated_text(text, target_language)
            dest_content.append(f'{line[:idx]}{trans_text}\n')

            state = "text"
            continue

        if line.startswith('> '):
            idx = line.find(' ') + 1
            line = line[idx:].lstrip()

        if state == "body":
            text = line
            trans_text = text_trans.get_translated_text(text, target_language)
            if trans_text:
                dest_content.append(f'{trans_text}\n')
            state = "text"
            continue

        if state == "text":
            text += ' ' + line
            trans_text = text_trans.get_translated_text(text, target_language)
            if trans_text:
                dest_content.append(f'{trans_text}\n')
            state = "text"
            continue

    return dest_content
# ---------------------------------------------------------------------------------------------------------------------------------

def translate_lang(base_path, target_language, text_trans):
    for root, dirs, files in os.walk(base_path):
        for filename in files:
            if filename.endswith('.md'):
                print(f'Converting file: {os.path.join(root, filename)}')

                with open(os.path.join(root, filename), 'r', encoding='utf-8') as fp:
                    file_text = fp.readlines()

                dest_text = translate_text(file_text, target_language, text_trans)

                with open(os.path.join(root, filename + '_dest.md'), 'w', encoding='utf-8') as fp:
                    fp.writelines(dest_text)

                break
# ---------------------------------------------------------------------------------------------------------------------------------

text_trans = TextTranslate('pt-br')
base_path = os.path.join(os.path.dirname(__file__), 'content/pt/docs')
# extract_ids(base_path, text_trans)
# text_trans.translate_text('en')
# text_trans.save_proj()

translate_lang(base_path, 'en', text_trans)
