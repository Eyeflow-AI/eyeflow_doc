#Copyright 2018 Google LLC
#
#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.
#
rm -rf public/
HUGO_ENV="production" hugo --gc || exit 1

PRESERVE="CNAME"

for fname in ../eyeflow_doc_public/*;
do
    if [[ $PRESERVE =~ (^|[[:space:]])$(basename "$fname")($|[[:space:]]) ]] ; then
        echo "Preserve: $fname"
    else
        echo "Remove: $fname"
        rm -rf $fname
    fi
done

cp -r ./public/* ../eyeflow_doc_public/.

cd ../eyeflow_doc_public
git add .
git commit -m "refresh"
git push
