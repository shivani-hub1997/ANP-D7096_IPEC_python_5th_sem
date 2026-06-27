"""Problem Statement 
A courier company calculates delivery charges based on the package weight. 
• Weight up to 2 kg → ₹50  
• Weight greater than 2 kg and up to 5 kg → ₹100  
• Weight greater than 5 kg → ₹180  
Write a Python program to display the delivery charge. 
Sample Input 
4 
Sample Output 
Delivery Charge = ₹100 
---------------------------------------------------------------"""

#--------------Coding Section----------------------------------#

#taking input from the user
weight = float(input("Enter the package weight(in kg): "))

#validate the weight of package
if(weight <=0):
    exit("Invalid Weight")

#checking the delivery charge from the weight

if(weight <= 2):
    print("Delivery Charge = ₹50")
elif(weight >2 and weight <= 5):
    print("Delivery Charge = ₹100")
else:
    print("Delivery Charge = ₹180")

#------------Output Section--------------------------------------

"""Output:
Enter the package weight(in kg): 3
-----------------------------------------------------------------
Delivery Charge = ₹100
-----------------------------------------------------------------"""