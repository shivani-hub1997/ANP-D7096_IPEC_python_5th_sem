"""Problem 1: Student Management System 
Problem Statement 
Create a class named Student to store and display a student's details. 
Requirements 
1. Create a class Student.  
2. Define the following instance variables:  
    o student_id  
    o name  
    o course  
    o marks  
3. Create a method accept_data() to take input from the user.  
4. Create a method display_data() to display all student details.  
5. Create another method check_result() that:  
    o Displays "Pass" if marks are 35 or above  
    o Displays "Fail" otherwise.  
6. Create an object of the class and call all the methods.  
Sample Input 
Enter Student ID : 101 
Enter Name : Rahul 
Enter Course : Python 
Enter Marks : 78 
Expected Output
------ Student Details ------ 
Student ID : 101 
Name       : Rahul 
Course     : Python 
Marks      : 78 
Result     : Pass""" 


#------------------------Coding Section------------------------------

class Student:
    # Method to accept student details
    def accept_data(self):
        self.student_id = int(input("Enter Student ID : "))
        self.name = input("Enter Name : ")
        self.course = input("Enter Course : ")
        self.marks = int(input("Enter Marks : "))

    # Method to check result
    def check_result(self):
        if self.marks >= 35:
            return "Pass"
        else:
            return "Fail"

    # Method to display student details
    def display_data(self):
        print("------ Student Details ------")
        print("Student ID :", self.student_id)
        print("Name       :", self.name)
        print("Course     :", self.course)
        print("Marks      :", self.marks)
        print("Result     :", self.check_result())


# Creating object of Student class
student1 = Student()

# Calling methods
student1.accept_data()
student1.display_data()


#----------------------Output---------------------------

"""
Enter Student ID : 101
Enter Name : Rahul
Enter Course : Python
Enter Marks : 78

------ Student Details ------
Student ID : 101
Name       : Rahul
Course     : Python
Marks      : 78
Result     : Pass
"""