import os
import toml
import yaml
import shutil
from collections import defaultdict
from pathlib import Path

basedir = Path('.')
if os.path.isdir(basedir / 'domains'): shutil.rmtree(basedir / 'domains')
os.mkdir(basedir / 'domains')

class SafeTomlDecoder(toml.TomlDecoder):
    def get_empty_inline_table(self): return dict()

for file in basedir.glob("*"):
    if str(file).endswith('.toml') and str(file).count('.') == 2:
        decoder = SafeTomlDecoder(dict)
        data = toml.load(file, decoder=decoder)
        print(data)

        if "@" in data:
            data[""] = data["@"]
            del data["@"]

        output = yaml.safe_dump(data)
        with open(basedir / 'domains' / str(file).replace('.toml', '.yaml'), 'w+') as output_file:
            output_file.write(output)
