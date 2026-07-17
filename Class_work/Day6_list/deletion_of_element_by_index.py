"""Proble statement : 
Write a Python program to delete an element from a list by index.
Ask the user for the index of the element to be deleted and display the updated list after deletion."""


#------------------------Coding Section---------------------------------

#Creating a List of 10 elements
list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

#Asking user for the index of the element to be deleted
index = int(input("Enter the index of the element to be deleted: "))

#verifying  the given index is valid or not
if index >= len(list):
    print("Invalid index. Please enter a valid index between 0 and", len(list)-1)


#If the index is valid, delete the element at that index
if index < len(list):
    deleted_element = list.pop(index)
    print("Deleted element:", deleted_element)
    print("Updated list after deletion:", list)


#---------------------------------output Section----------------------------------
""" 
Enter the index of the element to be deleted: 10
Invalid index. Please enter a valid index between 0 and 9


Enter the index of the element to be deleted: 7
Deleted element: 80
Updated list after deletion: [10, 20, 30, 40, 50, 60, 70, 90, 100]
"""    