import yaml
import pandas as pd

def read_yaml(yaml_path: str = 'src/config/config.yaml'):
    with open(yaml_path, 'r') as f:
        return yaml.load(f, Loader=yaml.SafeLoader)
    
def read_csv(csv_path: str):
    return pd.read_csv(csv_path)

def create_csv(df: pd.DataFrame,path:str):
    return df.to_csv(path, index= False)

def append_df_to_csv(df: pd.DataFrame, path: str):
    df.to_csv(path, header= False, index= False, mode= 'a')