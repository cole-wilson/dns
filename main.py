import os
import toml
import yaml
import shutil
from pathlib import Path

basedir = Path('.')

if os.path.isdir(basedir / 'domains'):
    shutil.rmtree(basedir / 'domains')
os.mkdir(basedir / 'domains')

for file in basedir.glob("*"):
    if str(file).endswith('.toml') and str(file).count('.') == 2:
        data = toml.load(file)

        if "@" in data:
            data[""] = data["@"]
            del data["@"]

        output = yaml.dump(data)

        with open(basedir / 'domains' / str(file).replace('.toml', '.yaml'), 'w+') as output_file:
            output_file.write(output)
