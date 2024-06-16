import pandas as pd

class CSVStrorageManager:
    def __init__(self) -> None:
        pass
    
    def read_csv(self,csv_path: str):
        return pd.read_csv(csv_path)
    
    def write_csv(self,df: pd.DataFrame,path:str):
        return df.to_csv(path, index= False)
    
    def append_df_to_csv(self,df: pd.DataFrame, path: str):
        df.to_csv(path, header= False, index= False, mode= 'a')
        
        
class StorageManager:
    def storage_func(self):
        csv_storage_manager = CSVStrorageManager()
        create_csv = csv_storage_manager.write_csv
        read_csv = csv_storage_manager.read_csv
        append_df_to_csv = csv_storage_manager.append_df_to_csv
        return create_csv, read_csv, append_df_to_csv