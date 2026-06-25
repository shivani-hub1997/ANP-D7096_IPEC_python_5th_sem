"""Write a Python program to find how many slices remain after equal distribution."""
"Coding Section"
Total_Pizza_Slice = int(input("Enter the number of slice: "))
Number_of_Children = int(input("Enter the number of children: "))
Remaining_Slice = Total_Pizza_Slice % Number_of_Children
"Output"
print(Remaining_Slice)