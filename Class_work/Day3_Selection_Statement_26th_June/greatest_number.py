''' Program to find out greatest number between two number'''
#input of first number from user
num1 = int(input("Enter first number : "))
#-----------------------------------------
#input of second number from the user
num2 = int(input("Enter second number : "))
#------------------------------------------
print("----------------------------------")
#finding the greatest
if(num1 > num2):
    print(num1,"is greater than",num2)
elif(num2 > num1):
    print(num2,"is greater than",num1)
else:
    print(num1,"and",num2,"are equal")
#--------------------------------------------
''' output: 
Enter first number : 34
Enter second number : 56
----------------------------------
56 is greater than 34
'''