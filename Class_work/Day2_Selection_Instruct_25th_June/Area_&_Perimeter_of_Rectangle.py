"""Write a program to calculate area and perimeter of rectangle and validate it"""

#input of length from the user
length = float(input("Enter the length of the rectangle (in meter): "))

#validating the length
if length < 0:
    print ("length cannot be negative")

    #--------------------------------------------------------------------
#input of breath fro the user
breath = float(input("Enter the breath of the rectangle (in meter): "))

#validating the breath
if breath < 0:
    print("breath cannot be negative")

    #--------------------------------------------------------------------


#Displaying the length to the user
print("The length is: ",length)

#Display the breath to the user
print("The breath is: ",breath)

#------------------------------------------------------------------------

#Displaying the area of rectangle 
print("The area of rectangle is: ", length*breath , "m^2")

#displaying the Perimeter of rectangle
print("The Perimeter of rectangle is: ",2*(length+breath) , "m")