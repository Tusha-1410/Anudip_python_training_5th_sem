present = 0
absent = 0

for i in range(1, 31):
    while True:
        status = input(f"Is student {i} present? (P/A): ").upper()

        if status == 'P':
            present += 1
            break
        elif status == 'A':
            absent += 1
            break
        else:
            print("Invalid input! Enter P for Present or A for Absent.")

print("\nTotal Present Students =", present)
print("Total Absent Students =", absent)
