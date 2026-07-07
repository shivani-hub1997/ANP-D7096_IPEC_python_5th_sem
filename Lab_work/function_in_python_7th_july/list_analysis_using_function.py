"""Problem Statement:
Write a Python program that defines the following functions: 
• find_max(numbers)  
• find_min(numbers)  
• find_average(numbers)  
The program should: 
• Accept a list of 10 integers from the user.  
• Call all three functions.  
• Display the maximum value, minimum value, and average of the list.
------------------------------------------------------------------------"""

#----------coding section-------------------------------#
#function to calculate maximum numbers
def find_max(numbers):
    return max(numbers)
#function to calculate minimum numbers
def find_min(numbers):
    return min(numbers)
#function to calculate average numbers
def find_average(numbers):
    sum = 0
    for i in range(len(numbers)+1):
        sum = sum + i
    average = sum/10
    return average

#---------------------------------------------------------
#main program
#creating a blank list
numbers = []

for i in range(10):
    num = int(input("Enter the numbers: "))
    numbers.append(num)

#displaying the list
print(numbers)

print("The maximum number in the list:",find_max(numbers))
print("The minimum number in the list: ",find_min(numbers))
print("The average number in the list: ",find_average(numbers))

#----------output section-----------------------------------#
"""
Output:
Enter the numbers: 1
Enter the numbers: 2
Enter the numbers: 3
Enter the numbers: 4
Enter the numbers: 5
Enter the numbers: 6
Enter the numbers: 7
Enter the numbers: 8
Enter the numbers: 9
Enter the numbers: 10

The maximum number in the list: 10
The minimum number in the list: 1
The average number in the list: 
--------------------------------------------------------------"""