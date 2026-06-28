"""  -------------------------Cybersecurity Login Validation---------------------- 
Problem Statement: 
A login system validates:
 • Username 
 • Password  
 • OTP  Conditions: 
      • All correct → Login Successful  
      • Incorrect OTP → Re-enter OTP  
      • Incorrect Password after 3 attempts → Account Locked  
      • Incorrect Username → User Not Found  
      
Sample Input 
Username: admin 
Password: admin123 
OTP: 4567 

Sample Output 
Login Successful 
Welcome Admin """


#------------------------------coding Section----------------------------------

# Taking input from the user
username = input("Enter Username: ")    
password = input("Enter Password: ")
otp = input("Enter OTP: ")

# Check if username is correct
if username == "admin":
    # Check if password is correct
    if password == "admin123":
        # Check if OTP is correct
        if otp == "4567":
            print("Login Successful")
            print("Welcome Admin")
        else:
            print("Incorrect OTP. Please re-enter OTP.")
    else:
        print("Incorrect Password. Account Locked after 3 attempts.")
else:
    print("User Not Found")

#------------------------------output section-----------------------------------------

"""
Sample Input
Username: admin
Password: admin123
OTP: 4567

Sample Output
Login Successful
Welcome Admin
"""