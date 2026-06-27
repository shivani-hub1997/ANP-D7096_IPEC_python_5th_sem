"""Problem Statement 
Only vehicles having a valid parking pass are allowed to enter a private parking area. 
Accept either 1 (Valid Pass) or 0 (No Pass). 
• If the input is 1, display: Entry Allowed 
• Otherwise display: Entry Denied 
-------------------------------------------
Sample Input 
0 
-------------------------------------------
Sample Output 
Entry Denied 
-------------------------------------------"""

#---------coding section------------------------#
#taking input from the user
input = int(input("Enter the input: "))

#validating the input
if(input <0 and input >1):
    exit("Invalid input")

#verify the input
if(input == 1):
    print("Entry Allowed")
else:
    print("Entry Denied")

#-----------output section----------------------
"""Output:
Enter the input: 1
------------------------------------------------
Entry Allowed
------------------------------------------------"""
