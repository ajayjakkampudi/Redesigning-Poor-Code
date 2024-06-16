import sys, os 
sys.path.append(os.path.join(os.getcwd(),'src'))

from dataclasses import dataclass
from utils.file_utils import read_yaml

paths = read_yaml()

# Initilizing the datapaths of database
@dataclass
class DataBasePaths:
    user_data_path = paths['user_data_path']
    book_data_path = paths['book_data_path']
    check_data_path = paths['check_data_path']

    