# to import mysql.connector module
import mysql.connector

# establish connection with mysql
dataconnection = mysql.connector.connect(
    host='localhost',
    user='root',
    password= 'sona@@',
    database='studentmangement'
)

# to create a cursor object
cursorobj = dataconnection.cursor()

# take input from user
student_id = input("Enter Student ID: ")
new_name = input("Enter New Student Name: ")
new_standard = input("Enter New Standard: ")

# writing update query
sql_query = "UPDATE student SET Stdname=%s, Standard=%s WHERE Stdid=%s"

# values to be updated
values = (new_name, new_standard, student_id)

# execute the update query
cursorobj.execute(sql_query, values)

# commit the changes
dataconnection.commit()

# check whether the record is updated
if cursorobj.rowcount > 0:
    print("Record Updated Successfully")
else:
    print("No Record Found with the Given Student ID")

# close cursor object
cursorobj.close()

# close connection object
dataconnection.close()