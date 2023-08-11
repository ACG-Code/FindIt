import glob
import os
import re

APP_NAME = 'FindIt'
APP_VERSION = '2.0.0'
EXTENSIONS = ['pro', 'rux', 'sub']


def main(**kwargs):
    output = []
    for extension in EXTENSIONS:
        search_pattern = os.path.join(kwargs['<datadir>'], '**', f'*.{extension}')
        files = glob.glob(search_pattern, recursive=True)
        for file_path in files:
            if os.path.isfile(file_path):
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    contents = f.read()
                    if re.search(kwargs['<string>'], contents):
                        output.append(file_path)
    if len(output) > 0:
        with open(kwargs['<outputfile>'], 'w') as f:
            for file in output:
                f.write(file)
                f.write('\n')
