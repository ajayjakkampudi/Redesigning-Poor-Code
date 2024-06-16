
def books_menu():
    print("\nManage Books")
    print("1. Add Books")
    print("2. Update Books")
    print("3. Delete Books")
    print("4. Search Books")
    print("5. List Books")
    print("6. Exit")
    try:
        choice = int(input("Enter Choice for managing Books: "))
        return choice
    except:
        books_menu()
    

def user_menu():
    print("\nManage User")
    print("1. Add User")
    print("2. Update User")
    print("3. Delete User")
    print("4. Search User")
    print("5. List User")
    print("6. Exit")
    try:
        choice = int(input("Enter Choice for managing Users: "))
    except:
        user_menu()
    return choice

def main_menu():
    print("\nLibrary Management System")
    print("1. Manage Books")
    print("2. Manage Users")
    print("3. Checkin Book")
    print("4. Checkout Book")
    print("5. Exit")
    try:
        choice = int(input("Enter choice: "))
        return choice
    except:
        main_menu()
    