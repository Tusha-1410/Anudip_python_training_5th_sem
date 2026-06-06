# Library Book Search System

# Each book record contains:
# Book Name and Number of Copies Available

books = [
    ("Python Basics", 5),
    ("Data Science", 0),
    ("Java Programming", 3),
    ("Machine Learning", 0)
]

# ----------------------------------------
# Task 1: Display Unavailable Books

print("Unavailable Books:")

for book in books:

    # book[1] contains number of copies
    if book[1] == 0:
        print(book[0])

print("-" * 40)

# ----------------------------------------
# Task 2: Find Books with More Than 2 Copies

print("Books with More Than 2 Copies:")

for book in books:

    if book[1] > 2:
        print(book[0], "-", book[1], "copies")

print("-" * 40)

# ----------------------------------------
# Task 3: Count Available Books

count = 0

for book in books:

    # A book is available if copies are greater than 0
    if book[1] > 0:
        count += 1

print("Available Books:", count)

print("-" * 40)

# ----------------------------------------
# Task 4: Stop Searching Once a Requested Book is Found

# Book to search
requested_book = "Java Programming"

found = False

for book in books:

    if book[0] == requested_book:

        print(requested_book, "Found in Library")
        found = True

        # Stop searching immediately
        break

if found == False:
    print(requested_book, "Not Available")

print("-" * 40)
