"""Problem Statement: 
Create a nested dictionary to store marks of students in three subjects. 
Example: 
{
'Rahul': {'Math': 85, 'Science': 90, 'English': 88},
'Priya': {'Math': 78, 'Science': 95, 'English': 82}, 
'Ankit': {'Math': 91, 'Science': 89, 'English': 94} } 
Write a program to: • Calculate the total marks of each student.  
• Calculate the average marks of each student.  
• Display the topper based on total marks.  
• Display the subject-wise highest marks along with the student's name.  
• Display students whose average is greater than or equal to 85. """

#---------coding section---------------------#
#Create an empty dictionary
students = {}

#Take input for 3 students
for i in range(3):
    name = input("Enter student name: ")

    math = int(input("Enter Math marks: "))
    science = int(input("Enter Science marks: "))
    english = int(input("Enter English marks: "))

    #Store marks in a nested dictionary
    students[name] = {
        "Math": math,
        "Science": science,
        "English": english
    }

#Display total and average of each student
print("Student Report:")

topper = ""
highest_total = 0

for name in students:
    total = students[name]["Math"] + students[name]["Science"] + students[name]["English"]
    average = total / 3

    print(name)
    print("Total =", total)
    print("Average =", average)

    #Find topper
    if total > highest_total:
        highest_total = total
        topper = name

#Display topper
print("Topper:")
print(topper, "with total marks =", highest_total)

#Find highest marks in each subject
subjects = ["Math", "Science", "English"]

print("Subject-wise Highest Marks:")

for subject in subjects:
    highest_marks = 0
    student_name = ""

    for name in students:
        if students[name][subject] > highest_marks:
            highest_marks = students[name][subject]
            student_name = name

    print(subject, ":", student_name, "-", highest_marks)

#Display students with average >= 85
print("Students with Average >= 85:")

for name in students:
    total = students[name]["Math"] + students[name]["Science"] + students[name]["English"]
    average = total / 3

    if average >= 85:
        print(name, ":", average)


#---------------------------------------output section----------------------------------------------------

"""
Enter student name: Rahul
Enter Math marks: 85
Enter Science marks: 90
Enter English marks: 88

Enter student name: Priya
Enter Math marks: 78
Enter Science marks: 95
Enter English marks: 82

Enter student name: Ankit
Enter Math marks: 91
Enter Science marks: 89
Enter English marks: 94

Student Report:
Rahul
Total = 263
Average = 87.67

Priya
Total = 255
Average = 85.0

Ankit
Total = 274
Average = 91.33

Topper:
Ankit with total marks = 274

Subject-wise Highest Marks:
Math : Ankit - 91
Science : Priya - 95
English : Ankit - 94

Students with Average >= 85:
Rahul : 87.66666666666667
Priya : 85.0
Ankit : 91.33333333333333"""