import json

# Open and read the JSON file
with open('students.json', 'r') as file:
    data = json.load(file)

# Access the list of students
students = data['students']

# Iterate through the list of students and print their details
for student in students:
    print(f"ID: {student['id']}")
    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print("Grades:")
    for subject, grade in student['grades'].items():
        print(f"  {subject}: {grade}")
    print()