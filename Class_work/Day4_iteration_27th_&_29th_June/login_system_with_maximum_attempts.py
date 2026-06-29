"""Problem Statement 
A system allows only three login attempts. 
The correct username is admin and the password is python123. 
If the credentials are correct, display "Login Successful". 
Otherwise, after three unsuccessful attempts, display "Account Locked". 
--------------------------------------------
Sample Output Attempt 1 
Username: admin 
Password: abc  
----------------------------------------------
Invalid Credentials  
----------------------------------------------
Attempt 2 
Username: admin 
Password: python123  
----------------------------------------------
Login Successful 
----------------------------------------------"""

#----------coding section---------------------

# Store the correct username and password
correct_username = "admin"
correct_password = "python123"

# Allow only 3 login attempts
for attempt in range(1, 4):
    print(f"\nAttempt {attempt}")

    # Accept username and password from the user
    username = input("Username: ")
    password = input("Password: ")

    # Check if both username and password are correct
    if username == correct_username and password == correct_password:
        print("Login Successful")
        break   # Exit the loop if login is successful

    else:
        # Invalid credentials
        print("Invalid Credentials")

        # If this is the third failed attempt, lock the account
        if attempt == 3:
            print("Account Locked")