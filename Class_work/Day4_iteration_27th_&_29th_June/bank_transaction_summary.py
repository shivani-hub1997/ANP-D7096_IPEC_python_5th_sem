"""Problem Statement 
A customer keeps entering transaction amounts. 
Positive numbers indicate deposits, while negative numbers indicate withdrawals. 
The customer enters 0 to finish. 
Display: 
• Total Deposit  
• Total Withdrawal  
• Final Balance  """

#----------coding section--------------------------
# Initialize variables
total_deposit = 0
total_withdrawal = 0
balance = 0

print("Enter transaction amounts.")
print("Use positive numbers for deposits, negative numbers for withdrawals.")
print("Enter 0 to finish.")

# Keep accepting transactions until the user enters 0
while True:
    amount = float(input("Enter transaction amount: "))

    # Stop the loop if 0 is entered
    if amount == 0:
        break

    # Check if the transaction is a deposit
    if amount > 0:
        total_deposit += amount
        balance += amount

    # Check if the transaction is a withdrawal
    else:
        total_withdrawal += abs(amount)   # Convert negative value to positive
        balance += amount                 # Subtracts from balance

# Display the results
print("\n----- Transaction Summary -----")
print("Total Deposit     :", total_deposit)
print("Total Withdrawal  :", total_withdrawal)
print("Final Balance     :", balance)