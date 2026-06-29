"""Problem Statement 
A teacher wants to analyze the marks of N students. 
Accept the marks of each student (out of 100).
Finally display: 
• Highest Marks  
• Lowest Marks  
• Average Marks  
• Number of students who passed (Marks ≥ 40)  
• Number of students who scored distinction (Marks ≥ 75)"""

#-----------coding section----------------------
# Accept the number of students
n = int(input("Enter the number of students: "))

# Initialize variables
total_marks = 0
highest_marks = 0
lowest_marks = 0
passed_students = 0
distinction_students = 0

# Read marks of each student
for i in range(1, n + 1):
    marks = float(input(f"Enter marks of student {i}: "))

    # Add marks to total
    total_marks += marks

    # Initialize highest and lowest marks with the first student's marks
    if i == 1:
        highest_marks = marks
        lowest_marks = marks
    else:
        # Check for highest marks
        if marks > highest_marks:
            highest_marks = marks

        # Check for lowest marks
        if marks < lowest_marks:
            lowest_marks = marks

    # Check if the student has passed
    if marks >= 40:
        passed_students += 1

    # Check if the student scored distinction
    if marks >= 75:
        distinction_students += 1

# Calculate average marks
average_marks = total_marks / n

# Display the results
print("\n----- Student Marks Analysis -----")
print("Highest Marks                 :", highest_marks)
print("Lowest Marks                  :", lowest_marks)
print("Average Marks                 :", average_marks)
print("Number of Passed Students     :", passed_students)
print("Number of Distinction Students:", distinction_students)