"""Problem Statement:
Write a Python program that defines a function calculate_grade(marks). 
The function should: 
• Accept marks (0–100) as a parameter.  
• Return the grade according to the following criteria:  
o 90 and above → A+  
o 75–89 → A  
o 60–74 → B  
o 40–59 → C  
o Below 40 → Fail  
The main program should: 
• Accept marks of 5 students.  
• Call the function for each student.  
• Display the marks and corresponding grade.
--------------------------------------------------------------------------"""

#------------coding section-----------------------------------#
#function to calculate marks of 5 student
def calculate_grade(marks):
    if marks>-90:
        return "A+"
    elif marks <=75:
        return "A"
    elif marks <=60:
        return "B"
    elif marks <=40:
        return "C"
    else:
        return "Fail"
#----------------------------------------------------------------
#main program
for i in range(1, 6):
    marks = float(input("Enter the marks of the student {i} (0-100): "))
    grade = calculate_grade(marks)
    print(f"Student {i}: Marks = {marks}, Grade = {grade}")

#----------output section----------------------------------------#
"""
Output:
Enter the marks of student 1 (0-100): 78
Student 1: Marks = 78.0, Grade = A
Enter the marks of student 2 (0-100): 60
Student 2: Marks = 60.0, Grade = B
Enter the marks of student 3 (0-100): 98
Student 3: Marks = 98.0, Grade = A+
Enter the marks of student 4 (0-100): 44
Student 4: Marks = 44.0, Grade = C
Enter the marks of student 5 (0-100): 23
Student 5: Marks = 23.0, Grade = Fail
-------------------------------------------------------------------"""