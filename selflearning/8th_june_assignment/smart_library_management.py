# Smart Library Management System

# The library dictionary stores book records keyed by book ID.
# Each book has a title, an author, and the number of copies available.
library = {
    "B101": {"title": "Python Basics", "author": "ABC", "copies": 5},
    "B102": {"title": "C Programming", "author": "XYZ", "copies": 4},
    "B103": {"title": "Java Fundamentals", "author": "PQR", "copies": 6},
    "B104": {"title": "Data Structures", "author": "LMN", "copies": 2},
    "B105": {"title": "DBMS", "author": "KLM", "copies": 0},
    "B106": {"title": "Operating Systems", "author": "RST", "copies": 3},
    "B107": {"title": "Computer Networks", "author": "UVW", "copies": 5},
    "B108": {"title": "Software Engineering", "author": "DEF", "copies": 1},
    "B109": {"title": "AI Basics", "author": "GHI", "copies": 4},
    "B110": {"title": "Machine Learning", "author": "JKL", "copies": 2},
    "B111": {"title": "Cyber Security", "author": "MNO", "copies": 7},
    "B112": {"title": "Cloud Computing", "author": "PST", "copies": 5},
    "B113": {"title": "Big Data", "author": "AAA", "copies": 3},
    "B114": {"title": "IoT", "author": "BBB", "copies": 2},
    "B115": {"title": "Blockchain", "author": "CCC", "copies": 1},
    "B116": {"title": "Web Development", "author": "DDD", "copies": 6},
    "B117": {"title": "HTML & CSS", "author": "EEE", "copies": 4},
    "B118": {"title": "JavaScript", "author": "FFF", "copies": 5},
    "B119": {"title": "React JS", "author": "GGG", "copies": 2},
    "B120": {"title": "Node JS", "author": "HHH", "copies": 3},
    "B121": {"title": "Django", "author": "III", "copies": 5},
    "B122": {"title": "Flask", "author": "JJJ", "copies": 1},
    "B123": {"title": "Android Dev", "author": "KKK", "copies": 4},
    "B124": {"title": "Data Science", "author": "LLL", "copies": 6},
    "B125": {"title": "Deep Learning", "author": "MMM", "copies": 2},
    "B126": {"title": "Ethical Hacking", "author": "NNN", "copies": 3},
    "B127": {"title": "Linux", "author": "OOO", "copies": 5},
    "B128": {"title": "Unix", "author": "PPP", "copies": 1},
    "B129": {"title": "Compiler Design", "author": "QQQ", "copies": 4},
    "B130": {"title": "Computer Graphics", "author": "RRR", "copies": 2}
}

# 1. Add a Book
# Get new book information from the user and add it to the library.
bid = input("Enter Book ID: ")
title = input("Enter Book Title: ")
author = input("Enter Author Name: ")
copies = int(input("Enter Copies: "))

library[bid] = {
    "title": title,
    "author": author,
    "copies": copies
}

print("Book Added Successfully")

# 2. Remove a Book
# Ask for the book ID and remove the record if it exists.
bid = input("\nEnter Book ID to Remove: ")

if bid in library:
    del library[bid]
    print("Book Removed")
else:
    print("Book Not Found")

# 3. Search Book by ID
# Look up a book by its ID and display its details.
bid = input("\nEnter Book ID to Search: ")

if bid in library:
    print(library[bid])
else:
    print("Book Not Found")

# 4. Search Book by Title
# Perform a case-insensitive title search across all books.
search_title = input("\nEnter Book Title: ")

found = False

for bid in library:

    if library[bid]["title"].lower() == search_title.lower():
        print(bid, library[bid])
        found = True

if found == False:
    print("Book Not Found")

# 5. Update Available Copies
# Change the stored number of copies for a specific book.
bid = input("\nEnter Book ID: ")

if bid in library:
    copies = int(input("Enter New Copies: "))
    library[bid]["copies"] = copies
    print("Copies Updated")
else:
    print("Book Not Found")

# 6. Issue a Book
# Decrease the available copy count when a book is issued.
bid = input("\nEnter Book ID to Issue: ")

if bid in library:

    if library[bid]["copies"] > 0:
        library[bid]["copies"] -= 1
        print("Book Issued Successfully")
    else:
        print("Book Not Available")

else:
    print("Book Not Found")

# 7. Return a Book
# Increase the available copy count when a book is returned.
bid = input("\nEnter Book ID to Return: ")

if bid in library:
    library[bid]["copies"] += 1
    print("Book Returned Successfully")
else:
    print("Book Not Found")

# 8. Books with fewer than 3 copies
# List books that are low on stock and may need restocking.
print("\nBOOKS WITH LESS THAN 3 COPIES")

for bid in library:

    if library[bid]["copies"] < 3:
        print(bid, library[bid])

# 9. Unavailable Books
# Show titles that are currently out of stock.
print("\nUNAVAILABLE BOOKS")

for bid in library:

    if library[bid]["copies"] == 0:
        print(bid, library[bid]["title"])

# 10. Most Available Book
# Determine which book has the highest number of copies available.
first = True

for bid in library:

    if first:
        most_available = bid
        first = False

    elif library[bid]["copies"] > library[most_available]["copies"]:
        most_available = bid

print("\nMOST AVAILABLE BOOK")
print(most_available, library[most_available])

# 11. Restocking Report
# Print a restocking report for books with fewer than 3 copies.
print("\nRESTOCKING REPORT")

for bid in library:

    if library[bid]["copies"] < 3:
        print(bid,
              library[bid]["title"],
              "Copies:",
              library[bid]["copies"])

# 12. Books Requiring Immediate Purchase
# Collect books that need immediate purchase because they have one or zero copies.
purchase_books = {}

for bid in library:

    if library[bid]["copies"] <= 1:
        purchase_books[bid] = library[bid]

print("\nBOOKS REQUIRING IMMEDIATE PURCHASE")

for bid in purchase_books:
    print(bid, purchase_books[bid])

# CHALLENGE: Library Summary Report

print("\n========== LIBRARY SUMMARY REPORT ==========")

print("Total Books =", len(library))

available_books = 0

for bid in library:
    available_books += library[bid]["copies"]

print("Total Copies Available =", available_books)

print("\nMost Available Book:")
print(most_available,
      library[most_available]["title"])

unavailable = 0

for bid in library:
    if library[bid]["copies"] == 0:
        unavailable += 1

print("Unavailable Books =", unavailable)

print("Books Requiring Purchase =",
      len(purchase_books))
