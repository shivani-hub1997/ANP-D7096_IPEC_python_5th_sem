"""Problem Statement 
A smartphone displays a low battery warning only when the battery percentage falls below 15%. 
Write a Python program to accept the battery percentage. 
If the battery is below 15, display: Connect Charger Immediately 
Otherwise, display nothing. 
Sample Input 
10 
Sample Output 
Connect Charger Immediately 
-----------------------------------------------------------------------"""

#--------------coding section--------------------------------------#
#taking input from the user
battery_percentage = int(input("Enter battery percentage: "))

#validating the battery_percentage
if(battery_percentage <0 or battery_percentage >100):
    exit("Invalid Data")

#Displaying the message
if(battery_percentage <15):
    print("Connect Charger Immediately")

#-------------output section-----------------------
"""Output:
Enter battery percentage: 12
Connect Charger Immediately
---------------------------------------------------"""