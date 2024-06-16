import sys, os
sys.path.append(os.path.join(os.getcwd(),'src'))

from codes.database import DatabaseConfig

def book_inputs() -> dict:
    """Inputs the value of columns on book manager by considering the columns dynamically from yaml file

    Returns:
        dict: returns the inputs in dict format
    """
    # Fetchs the columns of book manager from yaml file
    manager_book_cols = DatabaseConfig.book_manage_cols
    manager_book_vals = []
    
    # Inputs the values iterating through all cols
    for cols in manager_book_cols:
        if cols == 'availability': continue
        
        vals = str(input(f"Enter {cols}: "))        # Input
        vals = None if vals == '' else vals
        manager_book_vals.append(vals)
    
    # Mapping the input and output 
    data = dict(zip(manager_book_cols,manager_book_vals))
    return data

def user_inputs() -> dict:
    """Inputs the value of columns on user manager by considering the columns dynamically from yaml file

    Returns:
        dict: returns the inputs in dict format
    """
    # Fetchs the columns of book manager from yaml file
    manager_user_cols = DatabaseConfig.user_manage_cols
    manager_user_vals = []
    
    # Inputs the values iterating through all cols
    for cols in manager_user_cols:
        vals = str(input(f"Enter {cols}: "))
        vals = None if vals == '' else vals
        manager_user_vals.append(vals)
        
    # Mapping the input and output 
    data = dict(zip(manager_user_cols,manager_user_vals))
    return data

book_inputs()