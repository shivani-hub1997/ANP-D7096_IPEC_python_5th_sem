"""Problem Statement: 
Create a dictionary to store the marks of 5 students, where the key is the 
student's name and the value is their marks. 
Perform the following operations: 
• Display all student names and marks.  
• Add a new student with marks.  
• Update the marks of an existing student.  
• Delete a student by name.  
• Display the student who scored the highest marks."""

#---------coding section--------------------------#

#Create a dictionary for 5 students
students = {}

print("Enter details of 5 students:")
for i in range(5):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks

#Display all student names and marks
print("Student Marks:")
for name, marks in students.items():
    print(name, ":", marks)

#Add a new student
new_name = input("Enter new student name: ")
new_marks = int(input("Enter marks: "))
students[new_name] = new_marks

print("After Adding New Student:")
for name, marks in students.items():
    print(name, ":", marks)

#Update marks of an existing student
update_name = input("Enter the student name to update marks: ")

if update_name in students:
    new_marks = int(input("Enter new marks: "))
    students[update_name] = new_marks
    print("Marks updated successfully.")
else:
    print("Student not found.")

#Delete a student
delete_name = input("Enter the student name to delete: ")

if delete_name in students:
    del students[delete_name]
    print("Student deleted successfully.")
else:
    print("Student not found.")

#Display all students after update and delete
print("Updated Student Records:")
for name, marks in students.items():
    print(name, ":", marks)

#Display the student with the highest marks
highest_student = max(students, key=students.get)

print("Highest Scorer:")
print("Name :", highest_student)
print("Marks:", students[highest_student])

#--------output section----------------------------#
"""Output:
Enter details of 5 students: 
Enter student name: Kirti
Enter marks:72
Enter student name: Mihir
Enter marks:98
Enter student name: Aarav
Enter marks:89
Enter student name: Suhani
Enter marks: 87
Enter student name: Yashika
Enter marks:99

Students Marks:
Kirti : 72
Mihir : 98
Aarav : 89
Suhani : 87
Yashika : 99

Enter new student name: Pamila
Enter marks: 79

After Adding New Student:
Kirti : 72
Mihir : 98
Aarav : 89
Suhani : 87
Yashika : 99
Pamila : 79

Enter the student name to update marks: Suhani
Enter new marks: 80
Marks updated successfully.

Enter the student name to delete: Kirti
Student deleted successfully.

Updated Student Records:
Aarav : 89
Suhani : 80
Yashika : 99
Pamila : 79

Highest Scorer:
Name : Yashika
Marks: 99
"""