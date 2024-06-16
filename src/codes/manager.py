import sys, os
sys.path.append(os.path.join(os.getcwd(),'src'))

import pandas as pd
from abc import ABC, abstractmethod
from codes.database import DataBasePaths
from utils import file_utils
from utils.logger import logging

class Manager(ABC):
    @property
    @abstractmethod
    def _fetch(self):
        pass
    
    @abstractmethod
    def add(self, data: dict):
        pass
    
    @abstractmethod
    def update(self, data: dict):
        pass
    
    @abstractmethod
    def delete(self, data: dict):
        pass
    
    @abstractmethod
    def search(self, data: dict):
        pass
    
    @abstractmethod
    def list_values(self):
        pass
    
class BookManager(Manager):
    def __init__(self) -> None:
        self.__book_data_path = DataBasePaths.book_data_path    # private member
        self.__required_data = ['title', 'author', 'ISBN', 'availability']
        self._fetch

    @property
    def _fetch(self):
        # If .csv doesn't exist it will be created
        if not os.path.exists(self.__book_data_path):
            df = pd.DataFrame(columns=self.__required_data)
            file_utils.create_csv(df= df, path= self.__book_data_path)
            
        self.__book_data = file_utils.read_csv(self.__book_data_path)
        logging.info("Book Database was fetched")
        
        return self.__book_data
        
    def add(self, data: dict):
        data = {k:[v] for k,v in data.items()}
        data['availabilty'] = ['yes']
        print(data)
        added_df = pd.DataFrame(data)
        print(added_df)
        file_utils.append_df_to_csv(added_df, self.__book_data_path)
        logging.info(f"{data} data was added successfully")
        print("Data was added to book csv")
        self._fetch
    
    def update(self, isbn, data: dict):
        if not self.search({'ISBN': isbn}):
            print(f"No book was found with id {isbn}")
            
        for key, val in data.items():
            if val == None:
                continue
            
            self.__book_data.loc[self.__book_data['ISBN'] == isbn, key] = val
            
        file_utils.create_csv(df= self.__book_data, path= self.__book_data_path)
        logging.info(f"{data} Updated successfully")
        print("Updation was done")
    
    def delete(self, data):
        if not self.search(data):
            print("No such data found in the database to delete")
            return 
        cond = 1
        for key, val in data.items():
            if val == None:
                continue
            cond &= self.__book_data[key] == val

        self.__book_data = self.__book_data[~cond]
        file_utils.create_csv(df= self.__book_data, path= self.__book_data_path)
        logging.info(f"{data} deletion was done succefully")
        print("Deletion was done")
        
    def search(self, data: dict):
        cond = 1
        for key, val in data.items():
            if val == None:
                continue
            cond &= self.__book_data[key] == val
        print(cond)
        not_empty = self.__book_data[cond].shape[0] != 0
        value =  self.__book_data[cond] if not_empty else "No such data found in the database"
        print(value)
        
        return True if not_empty else False
    
    def list_values(self):
        return self._fetch
    
class UserManager(Manager):
    def __init__(self) -> None:
        self.__user_data_path = DataBasePaths.user_data_path    # private member
        self.__required_data = ['name', 'userid']
        self._fetch

    @property
    def _fetch(self):
        # If .csv doesn't exist it will be created
        if not os.path.exists(self.__user_data_path):
            df = pd.DataFrame(columns=self.__required_data)
            file_utils.create_csv(df= df, path= self.__user_data_path)
            
        self.__user_data = file_utils.read_csv(self.__user_data_path)
        logging.info("Book Database was fetched")
        
        return self.__user_data
        
    def add(self, data: dict):
        data = {k:[v] for k,v in data.items()}
        added_df = pd.DataFrame(data)
        file_utils.append_df_to_csv(added_df, self.__user_data_path)
        logging.info(f"{data} data was added successfully")
        print("Data was added to book csv")
        self._fetch
    
    def update(self, userid, data: dict):
        if not self.search({'userid': userid}):
            print(f"No book was found with id {userid}")
            
        for key, val in data.items():
            if val == None:
                continue
            
            self.__user_data.loc[self.__user_data['userid'] == userid, key] = val
            
        file_utils.create_csv(df= self.__user_data, path= self.__user_data_path)
        logging.info(f"{data} Updated successfully")
        print("Updation was done")
    
    def delete(self, data):
        if not self.search(data):
            print("No such data found in the database to delete")
            return 
        cond = 1
        for key, val in data.items():
            if val == None:
                continue
            cond &= self.__user_data[key] == val

        self.__user_data = self.__user_data[~cond]
        file_utils.create_csv(df= self.__user_data, path= self.__user_data_path)
        logging.info(f"{data} deletion was done succefully")
        print("Deletion was done")
        
    def search(self, data: dict):
        cond = 1
        for key, val in data.items():
            if val == None:
                continue
            cond &= self.__user_data[key] == val
        print(cond)
        not_empty = self.__user_data[cond].shape[0] != 0
        value =  self.__user_data[cond] if not_empty else "No such data found in the database"
        print(value)
        
        return True if not_empty else False
    
    def list_values(self):
        return self._fetch
        
# class UserManager(Manager):
#     def __init__(self) -> None:
#         pass      
        
def manager_objects(obj: str):
    objects = dict(
        manage_books = BookManager(),
        manage_users = UserManager()
    )       
    return objects[obj]
    
    

if __name__ == "__main__":
    bm = UserManager() 
    bm.search({'userid':'125'})
    # bm.update('123',{
    #     'title': 'wer',
    #     'author': None,
    #     'ISBN': None
    # })