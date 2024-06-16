import sys, os
sys.path.append(os.path.join(os.getcwd(),'src'))

import unittest
from codes.manager import BookManager, UserManager
from codes.database import DatabaseConfig

# Intiates the unit testing
class TestManage(unittest.TestCase):
    book_manager = BookManager()
    user_manager = UserManager()
    # Testing the add functinality
    def test_book_add(self):
        """
        Tests the add functionality of BookManger
        """
        data = dict(zip(DatabaseConfig.book_manage_cols,['A','a',1,'yes']))
        data = {k:v for k,v in data.items()}
        
        # adding data to database
        added_data = dict(self.book_manager.add(data).iloc[-1])
        # tests the the added is appended or not
        self.assertEqual(added_data, data)
        
    def test_user_add(self):
        """
        Tests the add functionality of UserManager
        """
        data = dict(zip(DatabaseConfig.user_manage_cols,['A',11]))
        data = {k:v for k,v in data.items()}
        
        # adding data to database
        added_data = dict(self.user_manager.add(data).iloc[-1])
        # tests the the added is appended or not
        self.assertEqual(added_data, data)
        
if __name__ == "__main__":
    unittest.main()