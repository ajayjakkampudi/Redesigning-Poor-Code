import yaml
import pandas as pd

def read_yaml(yaml_path: str = 'src/config/config.yaml'):
    with open(yaml_path, 'r') as f:
        return yaml.load(f, Loader=yaml.SafeLoader)
    
