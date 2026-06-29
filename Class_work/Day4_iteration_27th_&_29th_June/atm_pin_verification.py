"""Problem Statement 
An ATM allows a user to enter the correct PIN. The correct PIN is 4589. 
The user can keep entering the PIN until it matches the correct one. 
Display "Access Granted" when the correct PIN is entered. 
--------------------------------------------------------
Sample Output 
Enter PIN: 1234 
Incorrect PIN  
--------------------------------------------------------
Enter PIN: 9876 
Incorrect PIN  
-------------------------------------------------------
Enter PIN: 4589 
Access Granted 
-------------------------------------------------------"""

#-------------------coding section---------------------#
#correct pin
correct_pin = 4589

#taking input from the user
pin = int(input("Enter PIN: "))

while pin != correct_pin:
     print("Incorrect PIN")
     pin = int(input("Enter PIN: "))
print("Access Granted")