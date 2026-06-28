"""  2. Loan Approval System Problem Statement A bank evaluates loan applications using: 
• Credit Score ≥ 750  
• Annual Income ≥ ₹8,00,000  
• Existing Loan Amount ≤ ₹2,00,000  
Conditions: 
• All conditions satisfied → Approved  
• Only one condition fails → Manual Review  
• More than one condition fails → Rejected  

Sample Input 
Enter Credit Score: 780 
Enter Annual Income: 750000 
Enter Existing Loan Amount: 100000 

Sample Output 
Loan Status: Manual 
Review Reason: Income criteria not satisfied. """


#--------------------------Coding section---------------------------------


# Taking input from the user
credit_score = int(input("Enter Credit Score: "))
annual_income = int(input("Enter Annual Income: "))
existing_loan = int(input("Enter Existing Loan Amount: "))

# Variable to count the number of failed conditions
failed_conditions = 0

# Variable to store the reason(s) for failure
reason = ""

# Check Credit Score condition
if credit_score < 750:
    failed_conditions += 1
    reason += "Credit Score criteria not satisfied. "

# Check Annual Income condition
if annual_income < 800000:
    failed_conditions += 1
    reason += "Income criteria not satisfied. "

# Check Existing Loan Amount condition
if existing_loan > 200000:
    failed_conditions += 1
    reason += "Existing Loan Amount criteria not satisfied. "

# Decide the loan status based on the number of failed conditions
if failed_conditions == 0:
    # All conditions are satisfied
    print("Loan Status: Approved")

elif failed_conditions == 1:
    # Only one condition failed
    print("Loan Status: Manual Review")
    print("Review Reason:", reason)

else:
    # More than one condition failed
    print("Loan Status: Rejected")
    print("Reasons:", reason)


#--------------------------output section---------------------------------
""" 
Sample Input
Enter Credit Score: 780
Enter Annual Income: 750000
Enter Existing Loan Amount: 100000

Sample Output
Loan Status: Manual Review
Review Reason: Income criteria not satisfied. 

sample Input
Enter Credit Score: 700
Enter Annual Income: 70000
Enter Existing Loan Amount: 100000

sample Output
Loan Status: Rejected
Reasons: Credit Score criteria not satisfied. Income criteria not satisfied.
Existing Loan Amount criteria not satisfied. 
"""
