"""Write a Python program to determine how many complete rows can be formed."""
"Coding Section"
Total_Students = int(input("Enter the total number of students: "))
Students_per_Row = int(input("Enter the number of students in a row: "))
Number_of_Complete_Rows = Total_Students % Students_per_Row
"output"
print(Number_of_Complete_Rows)

