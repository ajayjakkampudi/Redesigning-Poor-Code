def book_inputs():
    title = str(input("Enter title: "))
    author = str(input("Enter author: "))
    isbn = str(input("Enter ISBN: "))
    data = {
        'title': None if title == '' else title,
        'author': None if author == '' else author,
        'ISBN': None if isbn == '' else isbn
    }
    return data

def user_inputs():
    user_name = str(input("Enter name: "))
    userid = str(input("Enter userid: "))
    data = {
        'name': None if user_name == '' else user_name,
        'userid': None if userid == '' else userid
    }
    return data