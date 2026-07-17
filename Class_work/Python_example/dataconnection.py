#to import mysql.connector module
import mysql.connector
#to establish connection with mysql
dataconnection = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'sona@@',
    database = 'studentmangement'
    )
#to create a cursor object
cursorobj = dataconnection.cursor()
#----------------------------------------------
#writing insert query
sql_query = 'insert into student values(%s,%s,%s,%s)'
#---------------------------------------------
'''
#put the values to be inserted
stdid = 'std101'
stdname = 'Anil'
standard = '10th'
age = 15
values =(stdid,stdname,standard,age)
#----------------------------------------------
#to execute the query
cursorobj.execute(sql_query,values)'''
#------------------------------------------
# multiple records to be inserted
values = [
    ('std102', 'Rahul', '9th', 14),
    ('std103', 'Priya', '10th', 15),
    ('std104', 'Neha', '8th', 13),
    ('std105', 'Aman', '9th', 14)
]
# execute the query for multiple records
cursorobj.executemany(sql_query, values)
#to commit changes
dataconnection.commit()
#---------------------------------------------
#to check data inserted or not
if (cursorobj.rowcount > 0):
    print("Data inserted successfully")
else:
    print("Unable to insert data")
#---------------------------------------------
#to close cursor object
cursorobj.close()
#to close connection object
dataconnection.close()
#---------------------------------------------