"""Write a Python program to calculate the value of money after a certain number of years assuming it doubles every year."""
"Coding Section"
Initial_Amount = float(input("Enter the initial amount: "))
Number_of_Years = int(input("Enter the number of years: "))
Final_Amount = Initial_Amount * (2**Number_of_Years)
"Output"
print(Final_Amount)