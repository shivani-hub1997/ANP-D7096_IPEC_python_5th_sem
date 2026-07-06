"""Problem Statement: Create a dictionary where: • Employee ID is the key.  
• Value is another dictionary containing:  
o Name  
o Department  
o Salary  Perform the following operations: 
• Display all employee details.  
• Search for an employee using Employee ID.  
• Increase the salary of all employees by 10%.  
• Display employees belonging to a specific department entered by the user.  
"""
#------------coding section--------------------#
# Create an empty dictionary
employees = {}

# Take input for 3 employees
for i in range(3):
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    dept = input("Enter Department: ")
    salary = float(input("Enter Salary: "))

    # Store employee details in a nested dictionary
    employees[emp_id] = {
        "Name": name,
        "Department": dept,
        "Salary": salary
    }

# Display all employee details
print("Employee Details:")
for emp_id in employees:
    print("Employee ID:", emp_id)
    print("Name:", employees[emp_id]["Name"])
    print("Department:", employees[emp_id]["Department"])
    print("Salary:", employees[emp_id]["Salary"])
    print()

# Search employee using Employee ID
search_id = input("Enter Employee ID to search: ")

if search_id in employees:
    print("Employee Found:")
    print(employees[search_id])
else:
    print("Employee not found.")

# Increase salary of all employees by 10%
for emp_id in employees:
    employees[emp_id]["Salary"] = employees[emp_id]["Salary"] * 1.10

print("After 10% Salary Increase:")
for emp_id in employees:
    print(emp_id, ":", employees[emp_id])

# Display employees of a specific department
department = input("Enter Department to search: ")

print("Employees in", department, "Department:")
for emp_id in employees:
    if employees[emp_id]["Department"] == department:
        print("Employee ID:", emp_id)
        print("Name:", employees[emp_id]["Name"])
        print("Salary:", employees[emp_id]["Salary"])
        print()


#-----------output section---------------------------------------#
"""Output:
Enter Employee ID: 5049654
Enter Name: Kiran
Enter Department: CSE     
Enter Salary: 50000
Enter Employee ID: 5454474
Enter Name: Raghav
Enter Department: ML
Enter Salary: 70000
Enter Employee ID: 507895
Enter Name: Vedansh
Enter Department: AI
Enter Salary: 55000

Employee Details:
Employee ID: 5049654
Name: Kiran
Department: CSE
Salary: 50000.0

Employee ID: 5454474
Name: Raghav
Department: ML
Salary: 70000.0

Employee ID: 507895
Name: Vedansh
Department: AI
Salary: 55000.0

Enter Employee ID to search: 5049654

Employee Found:
{'Name': 'Kiran', 'Department': 'CSE', 'Salary': 50000.0}

After 10% Salary Increase:
5049654 : {'Name': 'Kiran', 'Department': 'CSE', 'Salary': 55000.00000000001}
5454474 : {'Name': 'Raghav', 'Department': 'ML', 'Salary': 77000.0}
507895 : {'Name': 'Vedansh', 'Department': 'AI', 'Salary': 60500.00000000001}

Enter Department to search: ML

Employees in ML Department:
Employee ID: 5454474
Name: Raghav
Salary: 77000.0
"""