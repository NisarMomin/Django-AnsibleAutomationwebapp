import sys
from pathlib import Path

from ruamel.yaml import YAML

file_name = Path('sahil.yaml')

name = sys.argv[1]
#size = int(sys.argv[2])


yaml = YAML()
data = yaml.load(file_name)
data['tasks']['name'] = dict(yum=dict(name=name)
#data['yum'][name] = dict(name)
yaml.dump(data, sys.stdout)
yaml.dump(data, Path('sahil1.yaml'))
