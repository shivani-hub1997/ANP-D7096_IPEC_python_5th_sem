"""
problem statement: Write a python program to update an element in a list and display the updated list"""

#------------------------Coding Section---------------------------------

#Creating a List of 10 elements
list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]    

print("Original List:", list)

# Ask the user for the index of the element to be updated and the new value
index = int(input("Enter the index of the element to be updated: "))
new_value = int(input("Enter the new value: "))

#verifying the given index is valid or not
if index >= len(list):
    exit("Invalid index. Please enter a valid index between 0 and", len(list)-1)

# Update the element at the specified index
list[index] = new_value

# Display the updated list
print("Updated List:", list)


#-------------------------------output Section----------------------------------
""" 
Output 1:-
Original List: [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
Enter the index of the element to be updated: 3
Enter the new value: 45
Updated List: [10, 20, 30, 45, 50, 60, 70, 80, 90, 100]
"""