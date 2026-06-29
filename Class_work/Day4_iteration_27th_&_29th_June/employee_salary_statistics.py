"""Problem Statement 
A company has N employees. 
Accept the salary of each employee and determine: 
• Highest salary  
• Lowest salary  
• Average salary  
• Number of employees earning more than ₹50,000"""

#---------coding section-------------------
# Accept the number of employees
n = int(input("Enter the number of employees: "))

# Initialize variables
total_salary = 0
highest_salary = 0
lowest_salary = 0
count_above_50000 = 0

# Read salary of each employee
for i in range(1, n + 1):
    salary = float(input(f"Enter salary of employee {i}: ₹"))

    # Add salary to total
    total_salary += salary

    # Initialize highest and lowest salary with the first employee's salary
    if i == 1:
        highest_salary = salary
        lowest_salary = salary
    else:
        # Check for highest salary
        if salary > highest_salary:
            highest_salary = salary

        # Check for lowest salary
        if salary < lowest_salary:
            lowest_salary = salary

    # Count employees earning more than ₹50,000
    if salary > 50000:
        count_above_50000 += 1

# Calculate average salary
average_salary = total_salary / n

# Display the results
print("\n----- Employee Salary Analysis -----")
print("Highest Salary                : ₹", highest_salary)
print("Lowest Salary                 : ₹", lowest_salary)
print("Average Salary                : ₹", average_salary)
print("Employees earning above ₹50000:", count_above_50000)