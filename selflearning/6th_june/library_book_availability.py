# Library Book Availability

# Dictionary containing book names and number of copies
books = {
    "Python Basics": 5,
    "Data Structures": 0,
    "Machine Learning": 3,
    "Java Programming": 2,
    "DBMS": 0,
    "Operating Systems": 6,
    "Networking": 4,
    "Cloud Computing": 1,
    "Cyber Security": 0,
    "Web Development": 7
}

# ----------------------------------
# Task 1: Display books that are currently unavailable

print("Unavailable Books:")

for book in books:
    if books[book] == 0:
        print(book)

# ----------------------------------
# Task 2: Count the number of available books

available_count = 0

for book in books:
    if books[book] > 0:
        available_count += 1

print("\nNumber of Available Books:", available_count)

# ----------------------------------
# Task 3: Find the book with the maximum copies

max_book = ""
max_copies = 0

for book in books:
    if books[book] > max_copies:
        max_copies = books[book]
        max_book = book

print("\nBook with Maximum Copies:")
print(max_book, "-", max_copies)

# ----------------------------------
# Task 4: Create a list of books having less than 3 copies

low_stock_books = []

for book in books:
    if books[book] < 3:
        low_stock_books.append(book)

print("\nBooks Having Less Than 3 Copies:")
print(low_stock_books)

# ----------------------------------
# Task 5: Calculate the total number of books available

total_books = 0

for book in books:
    total_books = total_books + books[book]

print("\nTotal Number of Books Available:", total_books)
