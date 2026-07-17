# to import mysql.connector module
import mysql.connector

# establish connection with mysql
dataconnection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='sona@@',
    database='Studentmangement'
)

# to create a cursor object
cursorobj = dataconnection.cursor()

# take student id as input from user
student_id = input("Enter Student ID to Delete: ")

# writing delete query
sql_query = "DELETE FROM student WHERE Stdid=%s"

# value to be deleted
values = (student_id,)

# execute the delete query
cursorobj.execute(sql_query, values)

# commit the changes
dataconnection.commit()

# check whether the record is deleted
if cursorobj.rowcount > 0:
    print("Record Deleted Successfully")
else:
    print("No Record Found with the Given Student ID")

# close cursor object
cursorobj.close()

# close connection object
dataconnection.close()