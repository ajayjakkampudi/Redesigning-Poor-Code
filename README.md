### **Redesigning Poor Code**
The designed code for the Library Management System incorporates several key object-oriented programming principles, including inheritance, abstraction, and encapsulation, to ensure a robust and maintainable design. Each task within the system is divided into distinct modules, with each class and method specifically designed to perform a single responsibility. This modular approach enhances the scalability and maintainability of the system for future purposes.

Additionally, the system features a user-friendly Command Line Interface (CLI), allowing users to efficiently manage library data. The CLI is designed to provide an intuitive and seamless user experience, making library management tasks straightforward and accessible.

The functionalities of the design:
```yaml
# Choices for the user:
1. Manage Books
    - 1. Add Books
    - 2. Update Books
    - 3. Delete Books
    - 4. Search Books
    - 5. List Books
    - 6. Exit
2. Manage Users
    - 1. Add Users
    - 2. Update Users
    - 3. Delete Users
    - 4. Search Users
    - 5. List Users
    - 6. Exit
3. Checkin Book
4. Checkout Book
5. Availability of book
6. Exit")
```

1. All the required code in `src/codes` directory
    * `database.py`: this module contains the dataclass method which contains the global informations like paths, columns for Book csv and columns for user csv
    * `manage.py`: This module contains Usermanager and BookManager class which has a fuctionalities of add, update, search and list the data
    * `check.py`: This module contains the Check Module which utilized in checkin and checkout data
    * `menu.py`: This module prints the choices needed to manage the library as given in the above yaml file.
    * `input.py`: This modules have the methods which takes the inputs from user 
    * `storage.py`: This module contains the methods that are realted for CSV modifications

2. The overall code is thoroughly commented and documented to ensure clarity and ease of understanding. Each module, class, and method includes detailed comments explaining their purpose, functionality, and any important considerations. 

3. The project incorporates robust exception handling with a custom exception function defined in `utils/exception.py`. Additionally, logging is implemented to ensure that all relevant management activities are recorded. The logs are stored in the `logs/` directory, and the logging functionality is handled by `utils/logger.py`.

4. The project includes thorough unit testing for the `BookManager` object for add functionality, which is located in 'codes/test_manager.py'. This ensures that the core functionalities of the library management system are tested and verified for correctness.

5. For future-proofing, the classes in this project are designed to ensure maintainability and flexibility, allowing seamless addition of features such as new columns in book.csv or user.csv without altering existing functionality. This is achieved by configuring input values in a `config/config.yaml` file, enabling the code to adapt automatically.

6. In `manager.py`, the factory design pattern is utilized to facilitate the creation of objects managed within a dictionary structure.

7. Classes
    * `BookManager` & `UserManager`: The `BookManager` and UserManager classes inherit from an abstract class, each implementing essential methods such as add, update, search, fetch, and delete. Additionally, encapsulation is employed to protect certain instance variables within these classes. According to the functionality choosen add, delete, search, update: csv will be updated
    * `BookAvailability`: `BookAvailability` inherits from `BookManager`, utilizing its search method for efficient book availability management and to enhance maintainability, 
    * `CheckBooks`: This class has the functionalities like check-in and check-out. In check-out the book is borrowed, if it is borrowed availability is changed in book_manager and adds the user and book in `check_manager.csv`. In check-out the book returned the availability is changed and user borrow history will be deleted.


