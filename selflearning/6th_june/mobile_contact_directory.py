# Mobile Contact Directory

# Dictionary containing contact names and phone numbers
contacts = {
    "Amit": "9876543210",
    "Priya": "9876543211",
    "Rohan": "9876543212",
    "Neha": "9876543213",
    "Anjali": "9876543214",
    "Karan": "9876543215",
    "Pooja": "9876543216",
    "Arjun": "9876543217",
    "Sneha": "9876543218",
    "Rahul": "9876543219"
}

# ----------------------------------
# Task 1: Display all contact names in alphabetical order

print("Contact Names in Alphabetical Order:")

names = list(contacts.keys())
names.sort()

for name in names:
    print(name)

# ----------------------------------
# Task 2: Count the total number of contacts

count = 0

for name in contacts:
    count += 1

print("\nTotal Contacts:", count)

# ----------------------------------
# Task 3 & 5: Search for a contact and stop using break

search_name = input("\nEnter Contact Name to Search: ")

found = False

for name in contacts:
    if name == search_name:
        print("Contact Found")
        print("Phone Number:", contacts[name])
        found = True
        break   # Stop searching once found

if found == False:
    print("Contact Not Found")

# ----------------------------------
# Task 4: Create a list of contacts whose names start with a vowel

vowel_contacts = []

for name in contacts:
    if name[0] in "AEIOUaeiou":
        vowel_contacts.append(name)

print("\nContacts Starting with a Vowel:")
print(vowel_contacts)
