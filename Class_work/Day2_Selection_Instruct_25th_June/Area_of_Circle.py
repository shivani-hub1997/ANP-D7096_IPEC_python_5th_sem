"""Write a program to calculate area of circle and validate it"""

#Input of radius from the user
Radius = float(input("Enter the Radius of Cirlce (in meters): "))

#validating the Radius
if Radius < 0:
    print("Radius cannot be negative")

    #-----------------------------------------------------------------

    #Display the Radius to the user
    print("Radius is : ", Radius)

    #-----------------------------------------------------------------

    #display the area of circle to the user
    print("Area of Cirlce : ", 3.14* (Radius)^2)




