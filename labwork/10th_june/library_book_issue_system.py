# --------------------------------------------------
# Library Book Issue System
# --------------------------------------------------

# Function to read all books from file
# Each book record is stored as a comma-separated line: id,title,quantity
# The file is read into a list of book records, where each record is itself a list.
def read_books():

    file = open("books.txt", "r")

    books = []

    for line in file:

        line = line.strip()  # remove trailing newline characters

        data = line.split(",")  # split the line into [id, title, quantity]

        books.append(data)

    file.close()

    return books


# --------------------------------------------------
# Function to save updated books back to file
# This replaces the current contents of books.txt with the updated data.
def save_books(books):

    file = open("books.txt", "w")

    for book in books:

        line = book[0] + "," + book[1] + "," + book[2]

        file.write(line + "\n")

    file.close()


# --------------------------------------------------
# Function 1 : Display all books
# Reads the book list and prints each book's id, title, and available quantity.
def display_books():

    books = read_books()

    print("\nBook Records")

    for book in books:

        print("ID:", book[0],
              "| Title:", book[1],
              "| Quantity:", book[2])


# --------------------------------------------------
# Function 2 : Search Book by ID
# Prompts the user for a book id and prints matching details if found.
def search_book():

    book_id = input("Enter Book ID: ")

    books = read_books()

    found = False

    for book in books:

        if book[0] == book_id:

            print("\nBook Found")
            print("ID:", book[0])
            print("Title:", book[1])
            print("Quantity:", book[2])

            found = True
            break

    if found == False:
        print("Book Not Found")


# --------------------------------------------------
# Function 3 : Issue Book
# Decreases the quantity of the selected book by one if available.
def issue_book():

    book_id = input("Enter Book ID to Issue: ")

    books = read_books()

    found = False

    for book in books:

        if book[0] == book_id:

            quantity = int(book[2])  # convert available quantity to integer

            if quantity > 0:

                quantity -= 1

                book[2] = str(quantity)  # store quantity back as string

                save_books(books)

                print("Book Issued Successfully")

            else:

                print("Book Not Available")

            found = True
            break

    if found == False:
        print("Book ID Not Found")


# --------------------------------------------------
# Function 4 : Return Book
# Increases the quantity of the selected book by one and saves the update.
def return_book():

    book_id = input("Enter Book ID to Return: ")

    books = read_books()

    found = False

    for book in books:

        if book[0] == book_id:

            quantity = int(book[2])

            quantity += 1

            book[2] = str(quantity)

            save_books(books)

            print("Book Returned Successfully")

            found = True
            break

    if found == False:
        print("Book ID Not Found")


# --------------------------------------------------
# Function 5 : Display Unavailable Books
# Shows books that currently have zero copies available.
def unavailable_books():

    books = read_books()

    print("\nUnavailable Books")

    for book in books:

        if int(book[2]) == 0:

            print(book[0], "-", book[1])


# --------------------------------------------------
# Function 6 : Books Requiring Restocking
# Lists books with fewer than two copies available.
def restocking_books():

    books = read_books()

    print("\nBooks Requiring Restocking")

    for book in books:

        if int(book[2]) < 2:

            print(book[0],
                  "-",
                  book[1],
                  "- Copies:",
                  book[2])


# --------------------------------------------------
# Main Menu
# Repeatedly shows options until the user chooses to exit.
while True:

    print("\n")
    print("===== Library Book Issue System =====")
    print("1. Display All Books")
    print("2. Search Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Display Unavailable Books")
    print("6. Display Books Requiring Restocking")
    print("7. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        display_books()

    elif choice == 2:
        search_book()

    elif choice == 3:
        issue_book()

    elif choice == 4:
        return_book()

    elif choice == 5:
        unavailable_books()

    elif choice == 6:
        restocking_books()

    elif choice == 7:
        print("Thank You")
        break

    else:
        print("Invalid Choice")
