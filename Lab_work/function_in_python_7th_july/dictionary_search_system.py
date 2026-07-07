"""Problem Statement:
Write a Python program that defines a function search_student(student_dict, roll_no). 
The function should: 
• Accept a dictionary where:  
o Key = Roll Number  
o Value = Student Name  
• Search for the given roll number.  
• Return the student name if found; otherwise return "Student Not Found".  
The main program should: 
• Create a dictionary of at least 5 students.  
• Accept a roll number from the user.  
• Display the search result.
--------------------------------------------------------------------------------"""

#----------coding section-------------------------------#
# Function to search a student using roll number
def search_student(student_dict, roll_no):

    # Check if the roll number exists in the dictionary
    if roll_no in student_dict:
        return student_dict[roll_no]      # Return the student name
    else:
        return "Student Not Found"        # Return message if not found


# ---------------- Main Program ----------------

# Create a dictionary of students
# Key = Roll Number
# Value = Student Name
students = {
    101: "Rahul",
    102: "Priya",
    103: "Ankit",
    104: "Neha",
    105: "Aman"
}

# Accept the roll number from the user
roll_no = int(input("Enter Roll Number to search: "))

# Call the function and store the result
result = search_student(students, roll_no)

# Display the result
print("Search Result:", result)



#-------------------------------output section-------------------------------


"""
Enter Roll Number to search: 103
Search Result: Ankit

Enter Roll Number to search: 110
Search Result: Student Not Found
"""