"""-------------------Airline Ticket Pricing Engine-------------------------------------
. Airline Ticket Pricing Engine
Problem Statement
An airline calculates ticket fare using:
Base Fare = ₹5000
Additional Charges:
 Business Class → +₹3000
 Window Seat → +₹500
 Weekend Travel → +₹1000
Discounts:
 Age below 12 → 50%
 Age above 60 → 20%
Calculate the final ticket fare.

Sample Input
Enter Passenger Age: 65
 Business Class (Y/N): Y 
 Window Seat (Y/N): Y 
 Weekend Travel (Y/N): Y

Sample Output
Base Fare: ₹5000 
Additional Charges: ₹4500 
Senior Citizen Discount: 20% 
Final Ticket Fare: ₹7600.0
"""

# Base fare of the ticket
base_fare = 5000

# Additional charges initially set to 0
additional_charges = 0

# Taking input from the user
age = int(input("Enter Passenger Age: "))
business_class = input("Business Class (Y/N): ")
window_seat = input("Window Seat (Y/N): ")
weekend_travel = input("Weekend Travel (Y/N): ")

# Verify Business Class is selected
if business_class == "Y":
    additional_charges += 3000

# VerifyWindow Seat is selected
if window_seat == "Y":
    additional_charges += 500

# Verify Weekend Travel is selected
if weekend_travel == "Y":
    additional_charges += 1000

# Calculate total fare before discount
total_fare = base_fare + additional_charges

# Apply discount based on age
if age < 12:
    discount = total_fare * 0.50
    final_fare = total_fare - discount
   
    print("Child Discount: 50%")

elif age > 60:
    discount = total_fare * 0.20
    final_fare = total_fare - discount
   
    print("Senior Citizen Discount: 20%")

else:
    discount = 0
    final_fare = total_fare
    

# Display the results
print("Base Fare: ₹", base_fare)
print("Additional Charges: ₹", additional_charges)
print("Final Ticket Fare: ₹", final_fare)



#----------------------------------Output Section----------------------------------

"""
Sample Input
Enter Passenger Age: 65
 Business Class (Y/N): Y
 Window Seat (Y/N): Y
 Weekend Travel (Y/N): N

Sample Output
Senior Citizen Discount: 20%
Base Fare: ₹ 5000
Additional Charges: ₹ 4500
Final Ticket Fare: ₹ 7600.0
"""
