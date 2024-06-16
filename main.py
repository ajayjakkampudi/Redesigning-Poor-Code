# This is a deliberately poorly implemented main script for a Library Management System.
from src.codes.manager import BookManager, manager_objects
from src.codes.check import CheckBooks
from src.codes.inputs import book_inputs, user_inputs
from src.codes.menu import main_menu, books_menu, user_menu
from src.utils.logger import logging


def manage_books(choice: int):
    books_obj = manager_objects('manage_books')
    if choice == 1:
        print("Enter tile, author and ISBN number")
        data = book_inputs()
        books_obj.add(data)
        logging.info(f"{data} was added successfully")
        print("Data was added")
        
    elif choice == 2:
        print("Update the values by choosing ISBN value")
        isbn = str(input("Enter ISBN value: "))
        data = book_inputs()
        books_obj.update(isbn= isbn, data= data)
        logging.info(f"{data} was updated successfully")
        print("Data was updated")
        
    elif choice == 3:
        print("Enter data that to be deleted")
        data = book_inputs()
        books_obj.delete(data)
        logging.info(f"{data} was deleted successfully")
        print("Data was Deleted")
        
    elif choice == 4:
        print("Enter data that to be searched")
        data = book_inputs()
        res = books_obj.search(data)
        logging.info(f"{data}: data was searched")
        if res.empty == True: print("No such data was found")
        else:
            print(res)
        
    elif choice == 5:
        print("Books data")
        logging.info("Data fetched")
        print(books_obj.list_values())
        
    elif choice == 6:
        print('Exited')
        return
    else:
        print("Choose Correct Input")
        book_inputs()
        
def manage_users(choice: int):
    user_obj = manager_objects('manage_users')
    if choice == 1:
        print("Enter name and id")
        data = user_inputs()
        user_obj.add(data)
        logging.info(f"{data} User data added")
        print("Data Added")
        
    elif choice == 2:
        print("Update the values by choosing user id value")
        userid = str(input("Enter id: "))
        data = user_inputs()
        user_obj.update(userid= userid, data= data)
        logging.info(f"{data}: User data updated")
        print("Data Added")
        
    elif choice == 3:
        print("Enter data that to be deleted")
        data = user_inputs()
        user_obj.delete(data)
        logging.info(f"{data} was deleted successfully")
        print("Data was Deleted")
        
    elif choice == 4:
        print("Enter data that to be searched")
        data = user_inputs()
        res = user_obj.search(data)
        logging.info(f"{data}: data was searched")
        if res.empty == True: print("No such data was found")
        else:
            print(res)
        
    elif choice == 5:
        print("User data")
        logging.info("Data was fetched")
        print(user_obj.list_values())
        
    elif choice == 6:
        print('Exited')
        return
    else:
        print("Choose Correct Input")
        user_inputs()
    
        

def main():
    
    while True:
        choice = main_menu()
        if choice == 1:
            manage_books_choice = books_menu()
            manage_books(manage_books_choice)
   
        
        elif choice == 2:
            manage_user_choice = user_menu()
            manage_users(manage_user_choice)
        
        elif choice == 3:
            print("Enter details for checkin")
            userid = str(input("Enter userid: "))
            isbn = str(input("Enter ISBN value of Book: "))
            CheckBooks().check_in(userid= userid, isbn= isbn)
        elif choice == 4:
            print("Enter details for checkout")
            userid = str(input("Enter userid: "))
            isbn = str(input("Enter ISBN value of Book: "))
            CheckBooks().check_out(userid= userid, isbn= isbn)
        
        elif choice == 5:
            break
        else: 
            print("Chose option was invalid. Choose a correct option")
            continue
        
# def main():
#     while True:
#         choice = main_menu()
#         if choice == '1':
#             title = input("Enter title: ")
#             author = input("Enter author: ")
#             isbn = input("Enter ISBN: ")
#             book_management.add_book(title, author, isbn)
#             print("Book added.")
#         elif choice == '2':
#             book_management.list_books()
#         elif choice == '3':
#             name = input("Enter user name: ")
#             user_id = input("Enter user ID: ")
#             user_management.add_user(name, user_id)
#             print("User added.")
#         elif choice == '4':
#             user_id = input("Enter user ID: ")
#             isbn = input("Enter ISBN of the book to checkout: ")
#             checkout_management.checkout_book(user_id, isbn)
#             print("Book checked out.")
#         elif choice == '5':
#             print("Exiting.")
#             break
#         else:
#             print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
