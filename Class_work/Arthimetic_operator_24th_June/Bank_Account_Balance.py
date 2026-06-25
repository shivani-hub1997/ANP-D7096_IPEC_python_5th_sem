"""Write a Python program to calculate the remaining balance after withdrawal."""

"Coding Section"


Current_Balance = float(input("Enter the current amount: "))
Withdrawal_Amount = float(input("Enter the withdrawal amount: "))


Remaining_Balance = Current_Balance // Withdrawal_Amount


"Output"

print(Remaining_Balance)