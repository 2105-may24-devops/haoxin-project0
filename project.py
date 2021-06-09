# Store account information for login information comparison. 
# An account already exists, which is used to initially compare whether the username of the newly registered account already exists
member = [{"name": "admin", "pwd": "admin"}]
account = {}

# Store the book list for query and other operations
book_list = []
# Store the book number, used for subsequent operations to first identify 
# whether the entered book number is correct
book_id_list = []
# Store the book name, 
# used for subsequent operations to first identify whether the entered book name is correct
book_name_list = []
 
 
# Welcome page
def login_menu():
    while True:
        print("="*50)
        print("Welcome to the library Book system！")
        print("[1]sign up  [2]login in")
        login_request = input("please enter the option number:")
        if login_request in ["1", "2"]:
            if login_request == "1":
                register()
            if login_request == "2":
                login()
                break
        else:
            print("wrong entry, try it again: !")
 
 
# sign up
def register():
    print("="*50)
    print("Welcome to the sign up page:")
    register_name = input("Please enter the username:")
    for test_name in member:
        if register_name in test_name["name"]:
            print("Username already exist！")
            break
        register_pwd = input("Please enter the password:")
        if len(register_name) == 0 or len(register_pwd) == 0:
            print("the password entered is not confirm the requirement！")
        else:
            account["name"] = register_name
            account["pwd"] = register_pwd
            member.append(account)
            print("Sign up successfully! ")
            break
 
 
# login in
def login():
    while True:
        print("="*50)
        print("Welcome to the login in page!")
        login_name = input("Please enter the username:")
        login_pwd = input("Please enter the password:")
        if login_name == account["name"]and login_pwd == account["pwd"]:
            print("Login in successfully!")
            return
 
        else:
            print("Incorrect account or password, please re-enter！")
 
 

#main menu
def show_menu():
    while True:
        print("="*50)
        print("Welcome to log in to the library management system！")
        print("[1] Add books [2] Display all books [3] Modify books [4] Find books [5] Delete books [6] Exit the system")
        show_request = input("Please select a function：")
        if show_request == "1":
            add_book()
        elif show_request == "2":
            all_book()
        elif show_request == "3":
            update_book()
        elif show_request == "4":
            find_book()
        elif show_request == "5":
            del_book()
        elif show_request == "6":
            print("Logged out of the library management system！")
            break
        else:
            print("The input is wrong, please re-enter！")
 

#Add Book
def add_book():
    print("="*50)
    print("Welcome to the add book page！")
    book = {}
    add_id = input("Please enter the book number:")
    # 对重复图书编号进行提示
    if add_id not in book_id_list:
        add_name = input("Please enter the book name:")
        add_location = input("Please enter the book storage location:")
        book["id"] = add_id
        book_id_list.append(add_id)
        book["name"] = add_name
        book_name_list.append(add_name)
        book["location"] = add_location
        book_list.append(book)
        print("Add book successfully！")
        print()
    else:
        print("Number %s already exists！" % add_id)
 

#Show Book
def all_book():
    f = open("output.txt", "a")
    f.write("show all books")
    f.write("")
    for show_book in book_list:
        f.write("Book number: %s\nBook name: %s\nStorage location: %s" % (show_book["id"], show_book["name"], show_book["location"]))
        f.write("")
    f.close()
    print("="*50)
    print("Show all books")
    print()
    for show_book in book_list:
        print("Book number: %s\nBook name: %s\nStorage location: %s" % (show_book["id"], show_book["name"], show_book["location"]))
        print()

    

#Edit Book
def update_book():
    print("="*50)
    print("Welcome to the edit book page！")
    update_id = input("Please enter the book number: ")

    #Judge The Entered Book Number
    if update_id in book_id_list:
        for up_book in book_list:
            if up_book["id"] == update_id:
                up_location = input("Please enter a new location: ")
                up_book["location"] = up_location
                print("Successfully modified！")
 
    #Prompt for the Wrong Book Number Entered
    else:
        print("Book number does not exist！")
 
 

#To find a book, first query according to the book name, and then select one from the books of the same name(Enter the number)
def find_book():
    print("="*50)
    print("Welcome to the book query page！")

    #Story the result by query of book name
    fd_book_list = []
    while True:
        fd_name = input("Please enter the book name, return to the previous step and press N：")

        # exit operation options
        if fd_name == "N":
            break

        # Enter the name of the book correctly before querying
        if fd_name in book_name_list:
            print("search result")
            for fd_book in book_list:
                if fd_book["name"] == fd_name:
                    fd_book_list.append(fd_book)
                    book_id_list.append(fd_book["id"])
                    print("Book number %s\nBook name: %s\nStorage location：%s" % (fd_book["id"], fd_book["name"], fd_book["location"]))
                    print()
        # Prompt for incorrect book name input, and return to the book name input interface
        else:
            print("Book [%s] does not exist" % fd_name)
            continue
 
        # Select a book from the search results by book name and enter the book number
        while True:
            fd_new_id = input("Please select a book number, return to the previous step and press N：")
            if fd_new_id == "N":
                break

            # Enter the correct book number to continue the query
            if fd_new_id in book_id_list:
                print("search result")
                for fd_new_book in fd_book_list:
                    if fd_new_id == fd_new_book["id"]:
                        print("Book number: %s\nBook name: %s\nStorage location：%s" %
                              (fd_new_book["id"], fd_new_book["name"], fd_new_book["location"]))
                        print()

            #Tips for entering the wrong book number
            else:
                print("Book number [%s] does not exist" % fd_new_id)

                # Return to the interface for entering the book name
                break
 
 

# Delete Book
def del_book():
    print("=" * 50)
    print("Welcome to delete book page！")
    del_id = input("Please enter the book number：")
    if del_id in book_id_list:
        for de_book in book_list:
            if de_book["id"] == del_id:
                book_list.remove(de_book)
                print("successfully deleted！")
 

    # Prompt for the Wrong book number entered
    else:
        print("Book number does not exist！")
 
 
# Main Program
def main():
    login_menu()
    show_menu()
 
 
if __name__ == '__main__':
 main()