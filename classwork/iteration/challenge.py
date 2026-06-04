while True:
    marks = int(input("Enter Marks: "))

    if marks < 0 or marks > 100:
        print("Invalid Marks! Enter marks between 0 and 100.")
        continue

    if marks >= 40:
        print("Result: Pass")
        print("Congratulations! You have cleared the assessment.")
        break
    else:
        print("Result: Fail")