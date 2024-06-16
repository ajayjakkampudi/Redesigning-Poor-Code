import sys, os
sys.path.append(os.path.join(os.getcwd(),'src'))

import pandas as pd
from abc import ABC, abstractmethod
from codes.database import DatabaseConfig
from utils import file_utils
from utils.logger import logging
from codes.manager import BookManager, UserManager
from codes.storage import CSVStrorageManager, StorageManager

class CheckBooks(StorageManager):
    def __init__(self) -> None:
        super().__init__()
        self.create_csv, self.read_csv, self.append_df_to_csv = self.storage_func()
        self.__check_data_path = DatabaseConfig.check_data_path    # private member
        self.__book_data_path = DatabaseConfig.book_data_path
        self.__required_data = ['userid','borrowed_book_ISBN']
        self._book_manager = BookManager()
        self._user_manager = UserManager()
        self._fetch
    
    @property
    def _fetch(self):
        # If .csv doesn't exist it will be created
        if not os.path.exists(self.__check_data_path):
            df = pd.DataFrame(columns=self.__required_data)
            self.create_csv(df= df, path= self.__check_data_path)
            
        self.__check_data = self.read_csv(self.__check_data_path)
        self.__book_data = self._book_manager._fetch
        self.__user_data = self._user_manager._fetch
        logging.info("Database was fetched")
        
        return self.__check_data
    
    def book_availability(self, isbn: str):
        availability_ = True if (isbn in list(self.__book_data['ISBN'].astype(str))) & \
            any(self.__book_data[self.__book_data['ISBN'].astype(str) == isbn]['availability'] == 'yes') \
                else False
        return availability_
        
    def check_in(self,userid, isbn):
        check_data = {
            'userid': userid,
            'borrowed_book_ISBN': isbn
        }
        cond = (self.__check_data['userid'].astype(str) == userid) & \
            (self.__check_data['borrowed_book_ISBN'].astype(str) == isbn)
        if not any(cond):
            print("No such data is available please check the entries")
            return
        self.__check_data = self.__check_data[~cond]
        self.create_csv(self.__check_data, self.__check_data_path)
        
        self.__book_data.loc[self.__book_data['ISBN'].astype(str) == isbn, 'availability'] = 'yes'
        self.create_csv(self.__book_data, self.__book_data_path)
        self._fetch
    
    def check_out(self, userid: str, isbn):
        new_user = True if userid not in list(self.__user_data['userid'].astype(str)) else False
        user_data = {'name': None, 'userid':userid}
        if new_user:
            print("User not found please enter the user name to add into database")
            user_name = input("Enter user name: ")
            user_data['name'] = user_name
            user_data['userid'] = userid

            self._user_manager.add(user_data)
            
        availability = self.book_availability(isbn)
        if availability:
            data = dict(userid = [user_data['userid']], ISBN = [isbn])
            added_df = pd.DataFrame(data)
            self.append_df_to_csv(added_df, self.__check_data_path)
            self._book_manager.update(isbn, {'availability':['no']})
            logging.info(f"{data} data was added successfully")
            print("Data was added to book csv")
            self._fetch
            
        else:
            print("There no availabilty of book")
            
            
        