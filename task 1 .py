student_marks = {
    "Rishab": 85,
    "Riya": 92,
    "Vaikunth": 78,
    "Shobhna": 90,
    "Arpit": 88
}

student_name = input("Enter the student's name: ")

if student_name in student_marks:
    print(f"{student_name}'s marks: {student_marks[student_name]}")
else:
    print(f"Student '{student_name}' not found in the records.")
