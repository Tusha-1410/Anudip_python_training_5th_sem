# Employee ID Validation and Analysis System

# Taking Employee ID as input
emp_id = input("Enter Employee ID: ")

# ----------------------------------
# Task 1: Count uppercase letters

upper_count = 0

for ch in emp_id:
    if ch.isupper():
        upper_count += 1

print("\nUppercase Letters:", upper_count)

# ----------------------------------
# Task 2: Count digits

digit_count = 0

for ch in emp_id:
    if ch.isdigit():
        digit_count += 1

print("Digits:", digit_count)

# ----------------------------------
# Task 3: Extract joining year

joining_year = emp_id[3:7]

print("Joining Year:", joining_year)

# ----------------------------------
# Task 4: Extract employee name

employee_name = emp_id[7:-3]

print("Employee Name:", employee_name)

# ----------------------------------
# Task 5: Check ID validation rules

starts_with_emp = emp_id.startswith("EMP")

year_valid = emp_id[3:7].isdigit()

end_digits_valid = emp_id[-3:].isdigit()

if starts_with_emp and year_valid and end_digits_valid:
    valid = True
else:
    valid = False

# ----------------------------------
# Task 6: Create a list of all digits

digit_list = []

for ch in emp_id:
    if ch.isdigit():
        digit_list.append(int(ch))

print("Digit List:", digit_list)

# ----------------------------------
# Task 7: Find sum of all digits

digit_sum = 0

for num in digit_list:
    digit_sum += num

print("Sum of Digits:", digit_sum)

# ----------------------------------
# Task 8: Display ID status

if valid:
    print("ID Status: Valid")
else:
    print("ID Status: Invalid")
    