"""Problem Statement 
A supermarket allows a customer to purchase multiple products. 
The customer first enters the number of products. 
For each product, enter: 
• Product Name  
• Quantity  
• Price per Unit  
Finally display: 
• Individual Product Cost  
• Total Bill Amount  
• Most Expensive Product  
• Cheapest Product  
• Average Product Cost """

#------------coding section------------------------

# Accept the number of products
n = int(input("Enter the number of products: "))

# Initialize variables
total_bill = 0
highest_price = 0
lowest_price = 0
expensive_product = ""
cheap_product = ""

# Process each product
for i in range(1, n + 1):
    print("\nEnter details for Product", i)

    # Accept product details
    product_name = input("Product Name: ")
    quantity = int(input("Quantity: "))
    price = float(input("Price per Unit: "))

    # Calculate the cost of the product
    product_cost = quantity * price

    # Add product cost to total bill
    total_bill += product_cost

    # Display individual product cost
    print("Cost of", product_name, "=", product_cost)

    # Initialize highest and lowest price with the first product
    if i == 1:
        highest_price = price
        lowest_price = price
        expensive_product = product_name
        cheap_product = product_name
    else:
        # Check for most expensive product
        if price > highest_price:
            highest_price = price
            expensive_product = product_name

        # Check for cheapest product
        if price < lowest_price:
            lowest_price = price
            cheap_product = product_name

# Calculate average product cost
average_cost = total_bill / n

# Display the final results
print("\n----- Supermarket Bill Summary -----")
print("Total Bill Amount      :", total_bill)
print("Most Expensive Product :", expensive_product)
print("Cheapest Product       :", cheap_product)
print("Average Product Cost   :", average_cost)