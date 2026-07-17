"""Problem Statement 3 : Student Grade Calculator
A school assigns grades based on the marks obtained by students according to the following criteria:
* Marks 90 and above → Grade A
* Marks 75 to 89 → Grade B
* Marks 50 to 74 → Grade C
* Below 50 → Grade F
Write a Python program to accept marks from the user and display the corresponding grade.
Sample Input
Enter Marks: 92
Sample Output
Grade A
Sample Input
Enter Marks: 80
Sample Output
Grade B
Sample Input
Enter Marks: 65
Sample Output
Grade C
Sample Input
Enter Marks: 35
Sample Output
Grade F"""
#------------------------------------------------------------------------------------------------
#taking input from the user
marks = float(input("Enter the marks: "))
#validate input from the user
if(marks <0 or marks>100):
    exit("In valid marks")
#-----------------------------------------------------------------------------------------------
#Calculating grades for marks
if(marks >90):
    print("Grade A")
elif(marks >80 or marks <90):
    print("Grade B")
elif(marks >60 or marks <80):
    print("Grade C")
else:
    print("Grade F")

#--------------------------------------------------------------------------------------------
"""output :
Enter the marks: 72
-------------------------------------------------------------------------------------------
Grade C
-------------------------------------------------------------------------------------------"""