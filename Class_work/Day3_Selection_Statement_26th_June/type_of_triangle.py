'''------- Problem Statement: Display Type of Triangle Based On Angles

Write a Python program that accepts three angles (in degrees) from the user 
and check whether they form a valid triangle.
If they form a traingle then also display the type of triangle being formed.
-------------------------------------------------------------'''
#------- Coding ---------------
#input of first angle from the user
angle1 = float(input("Enter first angle(in degrees) :"))
#validate the angle
if(angle1 <= 0):
    exit("Angle must be positive")
#--------------------------------------------------------------
#input of second angle from the user
angle2 = float(input("Enter second angle(in degrees) :"))
#validate the angle
if(angle2 <= 0):
    exit("Angle must be positive")
#--------------------------------------------------------------
#input of third angle from the user
angle3 = float(input("Enter third angle(in degrees) :"))
#validate the angle
if(angle3 <= 0):
    exit("Angle must be positive")
#--------------------------------------------------------------
print("--------------------------------------------")
#to verify three angles form a triangle or not
if( angle1 + angle2 + angle3 == 180):
    #triangle is formed
    #acute angled triangled formation
    if(angle1 < 90 and angle2 < 90 and angle3 < 90):
        print("Above angles form acute angled triangle")
    #right angled trianlge
    elif(angle1 == 90 or angle2 == 90 or angle3 == 90):
        print("Above angles form right angled triangle")
    #Obtuse angled triangle
    else:
        print("Above angles form obtuse angled triangle")
else:
    print("Above angles do not form any triangle")

#----------------------------------------------------
'''Output : 
Enter first angle(in degrees) :45
Enter second angle(in degrees) :65
Enter third angle(in degrees) :70
--------------------------------------------
Above angles form acute angled triangle
--------------------------------------------'''