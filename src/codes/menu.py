
def books_menu() -> int:
    """Prints the choices required for managing books

    Returns:
        int: selected choice
    """
    print("\nManage Books")
    print("1. Add Books")
    print("2. Update Books")
    print("3. Delete Books")
    print("4. Search Books")
    print("5. List Books")
    print("6. Exit")
    
    # Checks whether choice in interger or not
    try:
        choice = input("Enter Choice for managing Books: ")
        choice = int(choice)
        return choice
    except:
        print(f"{choice} option is in valid, Enter valid choice")
        books_menu()
    

def user_menu() ->int:
    """Prints the choices required for managing users

    Returns:
        int: selected choice
    """
    print("\nManage User")
    print("1. Add User")
    print("2. Update User")
    print("3. Delete User")
    print("4. Search User")
    print("5. List User")
    print("6. Exit")
    # Checks whether choice in interger or not
    try:
        choice = input("Enter Choice for managing Users: ")
        choice = int(choice)
        return choice
    except:
        print(f"{choice} option is in valid, Enter valid choice")
        user_menu()
    

def main_menu() -> int:
    """Prints the choices required for managing (main menu)

    Returns:
        int: selected choice
    """
    print("\nLibrary Management System")
    print("1. Manage Books")
    print("2. Manage Users")
    print("3. Checkin Book")
    print("4. Checkout Book")
    print("5. Exit")
    
    # Checks whether choice in interger or not
    try:
        choice = input("Enter choice: ")
        choice = int(choice)
        return choice
    except:
        print(f"{choice} option is in valid, Enter valid choice")
        main_menu()
        
