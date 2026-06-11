#patient record management system
#Sample Input/Data (patients.txt) 
#P101,Anuj,Normal
#P102,Rahul,Critical
#P103,Priya,Stable
#P104,Neha,Critical
#P105,Amit,Stable
#P106,Sneha,Normal
#P107,Karan,Critical
#P108,Pooja,Stable
#P109,Rohit,Normal
#P110,Anjali,Stable

# --------------------------------------------------
# --------------------------------------------------
# Hospital Patient Record Management System
# --------------------------------------------------

# Function to read patient records from file
def read_patients():

    file = open("patients.txt", "r")

    patients = []

    for line in file:

        line = line.strip()      # Remove \n

        data = line.split(",")   # Convert into list

        patients.append(data)

    file.close()

    return patients


# --------------------------------------------------
# Task 1 : Display All Patient Records
# --------------------------------------------------

def display_patients():

    patients = read_patients()

    print("\nPatient Records")

    for patient in patients:

        print("ID:", patient[0],
              "| Name:", patient[1],
              "| Status:", patient[2])


# --------------------------------------------------
# Task 2 : Display Critical Patients
# --------------------------------------------------

def display_critical_patients():

    patients = read_patients()

    print("\nCritical Patients:")

    for patient in patients:

        if patient[2] == "Critical":

            print(patient[1])


# --------------------------------------------------
# Task 3 : Count Patients Under Each Status
# --------------------------------------------------

def count_patients():

    patients = read_patients()

    normal = 0
    stable = 0
    critical = 0

    for patient in patients:

        if patient[2] == "Normal":
            normal += 1

        elif patient[2] == "Stable":
            stable += 1

        elif patient[2] == "Critical":
            critical += 1

    print("\nPatient Count")
    print("Normal   :", normal)
    print("Stable   :", stable)
    print("Critical :", critical)


# --------------------------------------------------
# Task 4 : Search Patient by ID
# --------------------------------------------------

def search_patient():

    patient_id = input("Enter Patient ID: ")

    patients = read_patients()

    found = False

    for patient in patients:

        if patient[0] == patient_id:

            print("\nPatient Found:")
            print(patient[0] + "," +
                  patient[1] + "," +
                  patient[2])

            found = True

            break

    if found == False:

        print("Patient Not Found")


# --------------------------------------------------
# Task 5 : Save Critical Patients to File
# --------------------------------------------------

def save_critical_patients():

    patients = read_patients()

    file = open("critical_patients.txt", "w")

    for patient in patients:

        if patient[2] == "Critical":

            line = patient[0] + "," + patient[1] + "," + patient[2]

            file.write(line + "\n")

    file.close()

    print("Critical Patient Report Generated Successfully")


# --------------------------------------------------
# Main Menu
# --------------------------------------------------

while True:

    print("\n")
    print("===== Hospital Patient Record Management =====")
    print("1. Display All Patients")
    print("2. Display Critical Patients")
    print("3. Count Patients by Status")
    print("4. Search Patient by ID")
    print("5. Generate Critical Patient Report")
    print("6. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:

        display_patients()

    elif choice == 2:

        display_critical_patients()

    elif choice == 3:

        count_patients()

    elif choice == 4:

        search_patient()

    elif choice == 5:

        save_critical_patients()

    elif choice == 6:

        print("Thank You")
        break

    else:

        print("Invalid Choice")
        