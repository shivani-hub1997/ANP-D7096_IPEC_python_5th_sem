"""Problem Statement:
Write a function check_password(password) that checks whether a password is strong. 
A password is considered Strong if: 
• It contains at least 8 characters.  
• It contains at least one uppercase letter. 
• It contains at least one lowercase letter.  
• It contains at least one digit.  
The function should return: 
• "Strong Password" or  
• "Weak Password"  
The main program should accept a password from the user and display the result. 
--------------------------------------------------------------------------------"""

#------------coding section--------------------------------#
#function to check the password strength
def check_password(password):
    has_upper = False
    has_lower = False
    has_digit = False
    #Traverse each character of the password
    for ch in password:

        # Check if the character is an uppercase letter
        if 'A' <= ch <= 'Z':
            has_upper = True

        # Check if the character is a lowercase letter
        elif 'a' <= ch <= 'z':
            has_lower = True

        # Check if the character is a digit
        elif '0' <= ch <= '9':
            has_digit = True

    # Check all the conditions for a strong password
    if len(password) >= 8 and has_upper and has_lower and has_digit:
        return "Strong Password"
    else:
        return "Weak Password"

#------------------------------------------------------------
#main program

# Accept password from the user
password = input("Enter your password: ")

# Call the function and store the result
result = check_password(password)

# Display the result
print(result)

#--------------output section---------------------------------
"""Output:
Enter your password: Mihir
Weak Password
--------------------------------------------------------------"""
