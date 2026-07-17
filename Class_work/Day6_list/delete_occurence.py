""" 
write a program to crete a list of 20numbers given by user . 
Ask the user to input any other number if the number is present in list then 
remove its  duplicate occurences from the list but do not remove the first occurrence of that element and display the updated list after deletion."""



#--------------------------------------Coding Section---------------------------------

#Creating a  blank list
list = []

#Taking input 20 numbers  from the userand adding them to the list
for i in range(20):
    num = int(input("Enter a number: "))
    list.append(num)

#displaying the list
print("The list is: ", list)

print("--------------------------------------------------------------")

#displaying the numbers
print("The Numbers are : " )
for num in list:
    print(num, end=" ")

# Asking the user to input a number
num_to_remove = int(input("\nEnter a number to remove all occurrences of: "))

# Count the frequency of the number in the list
count = list.count(num_to_remove)

if count == 0:
    print("The number", num_to_remove, "is not present in the list.")
elif count == 1:
    print("The number", num_to_remove, "is present only once in the list. No duplicates to remove.")
else:
    #reverse the list to remove duplicates while keeping the first occurrence
    list.reverse()
    for i in range(1, count):
        list.remove(num_to_remove)
    list.reverse()

# Displaying the updated list after deletion
print("Updated list after removing duplicate occurrences of", num_to_remove, ":", list)

#---------------------------------output Section----------------------------------
"""
Output:
Enter a number: 10
Enter a number: 20
Enter a number: 30
Enter a number: 10
Enter a number: 40
Enter a number: 50
Enter a number: 10
Enter a number: 60
Enter a number: 70
Enter a number: 80
Enter a number: 90
Enter a number: 100
Enter a number: 10
Enter a number: 20
Enter a number: 30
Enter a number: 40
Enter a number: 50
Enter a number: 60  
Enter a number: 70
Enter a number: 80
The list is:  [10, 20, 30, 10, 40, 50, 10, 60, 70, 80, 90, 100, 10, 20, 30, 40, 50, 60, 70, 80]
--------------------------------------------------------------
The Numbers are :
10 20 30 10 40 50 10 60 70 80 90 100 10 20 30 40 50 60 70 80
Enter a number to remove all occurrences of: 10
Updated list after removing duplicate occurrences of 10 : [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 20, 30, 40, 50, 60, 70, 80]

"""