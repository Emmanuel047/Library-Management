import mysql.connector
mydb = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "root",
    database = "Library"
)

mycursor = mydb.cursor()
mycursor.execute("""
CREATE TABLE IF NOT EXISTS Books(
    id INT AUTO_INCREMENT PRIMARY KEY, 
    title VARCHAR(255), 
    author VARCHAR(255), 
    ISBN VARCHAR(255));""")
print("Succesfully Created the Database and Table - Books")


def add_books():
    book_name = input("Enter the name of the book: ")
    book_ISBN = input("Enter the ISBN of the book: ")
    book_Author = input("Enter the name of the Author of the Book: ")
    sql = "INSERT INTO Books(title, author, ISBN) VALUES(%s, %s, %s)"
    val = (book_name, book_Author, book_ISBN)
    mycursor.execute(sql, val)
    mydb.commit()
    print(f"Succesfully added {book_name}, {book_Author}, {book_ISBN} into the database.")
    print(mycursor.rowcount,"records added")

def view():
    mycursor.execute("SELECT * FROM Books")
    my_books = mycursor.fetchall()
    print("These are the books in the shelf:")
    for row in my_books:
        print(row)


def delete():
    del_book =int(input("Choose the index of the book from the list of books below."))
    available_books = mycursor.fetchall()
    for row in available_books:
        print(row)
    sql = f"DELETE FROM Books WHERE id = %s"
    mycursor.execute(sql, (del_book,))
    mycursor.commit()
    print(f"Succesfully Deleted Book with id {del_book}.")
    print(mycursor.rowcount,"records deleted.")

def search():
    search_book = input("Enter the name of the book you want to search for: ")
    sql = "SELECT * FROM Books WHERE title = %s"
    mycursor.execute(sql, (search_book,))
    result = mycursor.fetchall()
    if result:
        print("Book found")
        for row in result:
            print(row)
    else:
        print("No record was found")
    
def ui():
    print("Welcome to the Library Management System")
    while True:
        try:
            choice = int(input("1. Add Books.\n"
            "2. View Books.\n"
            "3. Delete Books.\n"
            "4. Search Books.\n"
            "5. Exit.\n"
            "Choose a commmand to execute: "))
        except ValueError as e:
            print("Enter a valid command from the list")
            return
        if choice == 1:
            add_books()
        elif choice == 2:
            view()
        elif choice == 3:
            delete()
        elif choice == 4:
            search()
        elif choice == 5:
            exit()
        else:
            print("Enter a valid no form the choice.")

ui()