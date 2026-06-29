"""Problem Statement
An electricity department wants to analyze electricity consumption of N houses. 
Accept the monthly units consumed by each house. 
Calculate and display: 
• Total units consumed  
• Average units consumed  
• Highest consumption  
• Lowest consumption """

#--------coding section---------------------------------#

# Accept the number of houses
n = int(input("Enter the number of houses: "))

# Initialize variables
total = 0
highest = 0
lowest = 0

# Read units consumed by each house
for i in range(1, n + 1):
    units = float(input(f"Enter units consumed by house {i}: "))

    # Add units to total
    total += units

    # Initialize highest and lowest with the first input
    if i == 1:
        highest = units
        lowest = units
    else:
        # Check for highest consumption
        if units > highest:
            highest = units

        # Check for lowest consumption
        if units < lowest:
            lowest = units

# Calculate average consumption
average = total / n

# Display the results
print("\n----- Electricity Bill Analysis -----")
print("Total Units Consumed   :", total)
print("Average Units Consumed :", average)
print("Highest Consumption    :", highest)
print("Lowest Consumption     :", lowest)