"""Write a Python program to calculate compound interest"""

#input from the user

Amount = float(input("Enter the final amount: "))
Principle = float(input("Enter the princilpe amount(in rs): "))
Rate = float(input("Enter the interest rate(anually): "))
Number = float((input("Enter the number of time: ")))
Time = int(input("Enter the time(in year): "))

#Displaying input to the user

print("Amount: ",Amount)
print("Principle: ",Principle)
print("Rate: ",Rate)
print("Number: ",Number)
print("Time: ", Time)

#Displaying output to the user

print("Compound Interest: ",(Amount = Principle(1+(Rate/Number))^Number*Time),compound interest = Amount - Principle)