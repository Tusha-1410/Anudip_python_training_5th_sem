# --------------------------------------------------
# Mobile Contact Directory System
# --------------------------------------------------

# Function to read contacts from file

def read_contacts():

    file = open("contacts.txt", "r")

    contacts = []

    for line in file:

        line = line.strip()

        data = line.split(",")

        contacts.append(data)

    file.close()

    return contacts


# --------------------------------------------------
# Function to save contacts back to file

def save_contacts(contacts):

    file = open("contacts.txt", "w")

    for contact in contacts:

        line = contact[0] + "," + contact[1]

        file.write(line + "\n")

    file.close()


# --------------------------------------------------
# Function 1 : Display All Contacts

def display_contacts():

    contacts = read_contacts()

    print("\nContact List")

    for contact in contacts:

        print("Name:", contact[0],
              "| Mobile:", contact[1])


# --------------------------------------------------
# Function 2 : Search Contact by Name

def search_contact():

    name = input("Enter Name to Search: ")

    contacts = read_contacts()

    found = False

    for contact in contacts:

        if contact[0].lower() == name.lower():

            print("\nContact Found")
            print("Name:", contact[0])
            print("Mobile:", contact[1])

            found = True
            break

    if found == False:
        print("Contact Not Found")


# --------------------------------------------------
# Function 3 : Add New Contact

def add_contact():

    name = input("Enter Name: ")
    mobile = input("Enter Mobile Number: ")

    contacts = read_contacts()

    contacts.append([name, mobile])

    save_contacts(contacts)

    print("Contact Added Successfully")


# --------------------------------------------------
# Function 4 : Update Contact Number

def update_contact():

    name = input("Enter Contact Name: ")

    contacts = read_contacts()

    found = False

    for contact in contacts:

        if contact[0].lower() == name.lower():

            new_number = input("Enter New Mobile Number: ")

            contact[1] = new_number

            save_contacts(contacts)

            print("Contact Updated Successfully")

            found = True
            break

    if found == False:
        print("Contact Not Found")


# --------------------------------------------------
# Function 5 : Delete Contact

def delete_contact():

    name = input("Enter Contact Name to Delete: ")

    contacts = read_contacts()

    found = False

    for contact in contacts:

        if contact[0].lower() == name.lower():

            contacts.remove(contact)

            save_contacts(contacts)

            print("Contact Deleted Successfully")

            found = True
            break

    if found == False:
        print("Contact Not Found")


# --------------------------------------------------
# Function 6 : Display Names Starting with Vowel

def contacts_starting_with_vowel():

    contacts = read_contacts()

    vowels = "AEIOUaeiou"

    print("\nContacts Starting With Vowel")

    for contact in contacts:

        if contact[0][0] in vowels:

            print(contact[0], "-", contact[1])


# --------------------------------------------------
# Main Menu

while True:

    print("\n")
    print("===== Mobile Contact Directory =====")
    print("1. Display All Contacts")
    print("2. Search Contact")
    print("3. Add Contact")
    print("4. Update Contact Number")
    print("5. Delete Contact")
    print("6. Contacts Starting With Vowel")
    print("7. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        display_contacts()

    elif choice == 2:
        search_contact()

    elif choice == 3:
        add_contact()

    elif choice == 4:
        update_contact()

    elif choice == 5:
        delete_contact()

    elif choice == 6:
        contacts_starting_with_vowel()

    elif choice == 7:
        print("Thank You")
        break

    else:
        print("Invalid Choice")
        