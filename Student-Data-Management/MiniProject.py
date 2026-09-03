# Count the Number of Student

numofStudents = int(input("Enter Total Students: "))

# Data Storage

studentData = []

# Inserting Data

for i in range(numofStudents):

    print(f"\nEnter the Data of Student {i+1}")

    name = input("Name: ")
    roll_no = int(input("Roll Number: "))
    marks = int(input("Marks: "))

    # Grade Calculation

    if marks > 95:
        grades = "A"
    elif marks > 80:
        grades = "B"
    elif marks > 60:
        grades = "C"
    elif marks >= 33:
        grades = "D"
    else:
        grades = "F"

    # Student Dictionary

    students = {
        "name": name,
        "roll_no": roll_no,
        "marks": marks,
        "grades": grades
    }

    # Store Student Data

    studentData.append(students)


# Data Printing

print("\nAll Students Data:")

for s in studentData:
    print(
        f"{s['name']} - Roll Number: {s['roll_no']} "
        f"- Marks: {s['marks']} - Grades: {s['grades']}"
    )


# Passed Students

print("\nStudents Who Are Passed:")

for s in studentData:

    if s["marks"] >= 33:
        print(f"{s['name']} - Marks: {s['marks']}")