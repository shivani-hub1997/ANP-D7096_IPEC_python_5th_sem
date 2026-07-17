"""Write a program to create a list of 20 numbers given by user.
Ask the user to input any other number.
If the number is present in list then remove it's all duplicates occurences from the list."""

#-----------coding section--------------------
#creting a blank list
numbers = []
print("Enter any 20 numbers: ")

for x in range (20):
    #input of element from user
    num = int(input())
    #inserting data in list at end
    numbers.append(num)
#------------------------------------
print("----------------------")
print("Numbers are: ",numbers)

#taking input from the user
element = int(input("Enter the new number: "))

#to find frequency
fred = numbers.count(element)
if(fred == 0):
    print(element,"not found")
elif(fred == 1):
    print("No duplicates found")
else:
    numbers.reverse()
    print(numbers)

    for x in range (1,fred):
        numbers.remove(element)
    numbers.reverse()
print(numbers)
