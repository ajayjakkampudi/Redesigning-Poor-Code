import sys, os
sys.path.append(os.path.join(os.getcwd(),'src'))

import pandas as pd
from utils.exception import CustomeException
# Methods required to modify CSV files
class CSVStrorageManager:
    # Read csv from given path
    def read_csv(self,csv_path: str):
        try:
            return pd.read_csv(csv_path)
        except CustomeException as ce:
            raise ce
    # Saves csv in the path
    def write_csv(self,df: pd.DataFrame,path:str):
        try:
            return df.to_csv(path, index= False)
        except CustomeException as ce:
            raise ce
    # appends data to csv
    def append_df_to_csv(self,df: pd.DataFrame, path: str):
        try:
            df.to_csv(path, header= False, index= False, mode= 'a')
        except CustomeException as ce:
            raise ce
        
# Specifies the methods of csv
class StorageManager:
    def storage_func(self):
        csv_storage_manager = CSVStrorageManager()
        create_csv = csv_storage_manager.write_csv
        read_csv = csv_storage_manager.read_csv
        append_df_to_csv = csv_storage_manager.append_df_to_csv
        return create_csv, read_csv, append_df_to_csv