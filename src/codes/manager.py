import sys, os
sys.path.append(os.path.join(os.getcwd(),'src'))

import pandas as pd
from abc import ABC, abstractmethod
from codes.database import DatabaseConfig
from utils import file_utils
from utils.logger import logging
from utils.exception import CustomeException
from codes.storage import CSVStrorageManager, StorageManager


        
# Abstarct Manager Class
class Manager(ABC, StorageManager):
    def __init__(self) -> None:
        super().__init__()
        # methods to modify csv or json
        self.create_csv, self.read_csv, self.append_df_to_csv = self.storage_func()
    @property
    @abstractmethod
    def _fetch(self):
        pass
    
    @abstractmethod
    def add(self, data: dict):
        pass
    
    @abstractmethod
    def update(self,isbn, data: dict):
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


# Book Manager Class
class BookManager(Manager):
    def __init__(self) -> None:
        # Intializing data path and columns
        super().__init__()
        self.__book_data_path = DatabaseConfig.book_data_path    # private member
        self.__required_cols = DatabaseConfig.book_manage_cols
        self._fetch

    @property
    def _fetch(self) -> pd.DataFrame:
        """Fetches the Book database if exists else creates empty csv

        Returns:
            pd.DataFrame: returns database
        """
        # If .csv doesn't exist, csv is created with required columns
        if not os.path.exists(self.__book_data_path):
            df = pd.DataFrame(columns=self.__required_cols)
            self.create_csv(df= df, path= self.__book_data_path)
        
        # Reading the csv
        self.__book_data = self.read_csv(self.__book_data_path)
        # Converts the columns data type to object
        self.__book_data = self.__book_data.astype({col: 'object' for col in self.__book_data.columns})        
        return self.__book_data
        
    def add(self, data: dict) -> pd.DataFrame:
        """Add the data

        Args:
            data (dict): data dictionary to be addded

        Returns:
            pd.DataFrame: return book database
        """
        try:
            data = {k:[v] for k,v in data.items()}
            # If data is the book is available
            data['availability'] = ['yes']
            added_df = pd.DataFrame(data)
            
            # Appending the data to csv
            self.append_df_to_csv(added_df, self.__book_data_path)
            print(f"{data} Data added successfully")
            logging.info(f"{data} added successfully")
            
            # re-initialized database
            self._fetch
            
            return self.__book_data
        
        except CustomeException as ce:
            raise ce
    
    def update(self, isbn: str, data: dict):
        """Updates the values provided by user wrt finding the unique unique ISBN value

        Args:
            isbn (str): Unique ISBN value used for searching and updating
            data (dict): updates the provided values ignores the unprovided value
        """
        if self.search({'ISBN': isbn}).empty == True:
            print(f"No book was found with ISBN {isbn}")
            return
        try:
            for key, val in data.items():
                if val == None: continue
                # updates the values
                self.__book_data.loc[self.__book_data['ISBN'].astype(str) == isbn, key] = val
                
            self.create_csv(df= self.__book_data, path= self.__book_data_path)
            print(f"Database was updates with {data}")
            logging.info(f"Database was updates with {data}")
            
        except CustomeException as ce:
            raise ce
        
    def delete(self, data: dict):
        """Deletes the row containing the provided data

        Args:
            data (dict): data dictionary needed to be deleted
        """
        if self.search(data).empty == True:
            print("No such data found in the database to delete")
            return 
        
        try:
            cond = 1
            for key, val in data.items():
                if val == None:
                    continue
                # gets truth table
                cond &= self.__book_data[key].astype(str) == val

            # Deletes the rows
            self.__book_data = self.__book_data[~cond]
            self.create_csv(df= self.__book_data, path= self.__book_data_path)
            print(f"{data} was deleted from book database")
            logging.info(f"{data} was deleted from book database")
            self._fetch
            
        except CustomeException as ce:
            print(ce)
        
    def search(self, data: dict) -> pd.DataFrame:
        """searching the given data in databse

        Args:
            data (dict): data need to be searched

        Returns:
            pd.DataFrame: fetched searching data
        """
        try:
            cond = 1
            for key, val in data.items():
                if val == None:
                    continue
                # Get truth table
                cond &= self.__book_data[key].astype(str) == val
            # Searching data
            res = self.__book_data[cond]
            if res.empty:
                print(f"{data} was not found in databse")
                logging.info(f"{data} was not found in databse")
            else:
                print(f"{data} was found in databse")
                logging.info(f"{data} was found in databse")
                
            return res
        
        except CustomeException as ce:
            print(ce)
    
    def list_values(self):
        # fetches the database
        print("Database fetched")
        logging.info("Book Database was fetched")
        return self._fetch
    
class UserManager(Manager):
    def __init__(self) -> None:
        super().__init__()
        self.__user_data_path = DatabaseConfig.user_data_path    # private member
        self.__required_cols = DatabaseConfig.user_manage_cols
        self._fetch

    @property
    def _fetch(self):
        """Fetches the user database if exists else creates empty csv

        Returns:
            pd.DataFrame: returns database
        """
        # If .csv doesn't exist it will be created
        if not os.path.exists(self.__user_data_path):
            df = pd.DataFrame(columns=self.__required_cols)
            self.create_csv(df= df, path= self.__user_data_path)
            
        self.__user_data = self.read_csv(self.__user_data_path)
        # converting all columns to object type
        self.__user_data = self.__user_data.astype({col: 'object' for col in self.__user_data.columns})
        return self.__user_data
        
    def add(self, data: dict):
        """Add the data

        Args:
            data (dict): data dictionary to be addded

        Returns:
            pd.DataFrame: return user database
        """
        try:
            data = {k:[v] for k,v in data.items()}
            added_df = pd.DataFrame(data)
            
            # datais appended to csv
            self.append_df_to_csv(added_df, self.__user_data_path)
            print(f"{data} Data added successfully")
            logging.info(f"{data} added successfully")
            self._fetch
            return self.__user_data
        
        except Exception as ce:
            print(ce)
    
    def update(self, userid, data: dict):
        """Updates the values provided by user wrt finding the unique userid value

        Args:
            userid (str): Unique userid value used for searching and updating
            data (dict): updates the provided values ignores the unprovided value
        """
        if self.search({'userid': userid}).empty == True:
            print(f"No user was found with userid {userid}")
            return
        try: 
            for key, val in data.items():
                if val == None:
                    continue
                # updates
                self.__user_data.loc[self.__user_data['userid'].astype(str) == userid, key] = val
                
            self.create_csv(df= self.__user_data, path= self.__user_data_path)
            print(f"User Database was updates with {data}")
            logging.info(f"User Database was updates with {data}")
            
        except CustomeException as ce:
            print(ce)
    
    def delete(self, data):
        """Deletes the user row containing the provided data

        Args:
            data (dict): data dictionary needed to be deleted
        """
        if self.search(data).empty == True:
            print("No such data found in the database to delete")
            return 
        
        try:
            cond = 1
            for key, val in data.items():
                if val == None:
                    continue
                cond &= self.__user_data[key].astype(str) == val
            # deletes
            self.__user_data = self.__user_data[~cond]
            self.create_csv(df= self.__user_data, path= self.__user_data_path)
            print(f"{data} was deleted from user database")
            logging.info(f"{data} was deleted from user database")
            self._fetch
            
        except CustomeException as ce:
            print(ce)
        
    def search(self, data: dict):
        """searching the given data in databse

        Args:
            data (dict): data need to be searched

        Returns:
            pd.DataFrame: fetched searching data
        """
        try:
            cond = 1
            for key, val in data.items():
                if val == None:
                    continue
                cond &= self.__user_data[key].astype(str) == val
            res =  self.__user_data[cond]
            if res.empty:
                print(f"{data} was not found in user databse")
                logging.info(f"{data} was not found in user databse")
            else:
                print(f"{data} was not found in user databse")
                logging.info(f"{data} was not found in user databse")
                
            return res
        
        except CustomeException as ce:
            print(ce)
    
    def list_values(self):
        logging.info("Book Database was fetched")
        print("Fetches the user datbase")
        return self._fetch
        
class Availability(BookManager):
    def __init__(self) -> None:
        super().__init__()
        
    def book_available(self,isbn: str):
        """Check the availability using the isbn value

        Args:
            isbn (str): Unique value to identify books

        Returns: If book are available the returns the books
        """
        book_data = self.list_values()
        data = {"ISBN":isbn}
        available_books = self.search(data)
        
        if available_books.empty:
            return
        
        available_books = available_books[available_books['availability'] == 'yes'] 
        print(f"{data} data checking availability is completed")
        logging.info(f"{data} data checking availability is completed")
        return available_books if not available_books.empty else "Book is not available"


def manager_objects(obj: str):
    objects = dict(
        manage_books = BookManager(),
        manage_users = UserManager(),
        availability = Availability()
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