import sys, os 
sys.path.append(os.path.join(os.getcwd(),'src'))

from dataclasses import dataclass
from utils.file_utils import read_yaml

# reading confing.yaml
config = read_yaml()

# Initilizing the data in yaml files
@dataclass
class DatabaseConfig:
    user_data_path = config['user_data_path']
    book_data_path = config['book_data_path']
    check_data_path = config['check_data_path']
    book_manage_cols = config['book_manager_columns']
    user_manage_cols = config['user_manager_columns']

    