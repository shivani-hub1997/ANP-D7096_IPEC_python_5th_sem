#importing module
import twodfigures
#Loop runs until the user choose Exit
while True:
#-----------------------------------------
#Displaying the main menu
    print("Selecting one of the following figure:")
    print("1 Square")
    print("2 Circle")
    print("3 Triangle")
    print("4 Rectangle")
    print("5 Exit")

    #taking user choice
    choice = int(input("Enter your choice: "))
    #User want Exit
    if choice == 5:
        print("Thanks!")
        break
    #User select square
    if choice == 1:
        side = float(input("Enter side of square: "))
    #------------------------------------------
        print("1 Area")
        print("2 Perimeter")
        op = int(input("Choose operation: "))
    #------------------------------------------
        #calculating operations on square
        if op == 1:
            print("Area of Square =", twodfigures.square_area(side))
        elif op == 2:
            print("Perimeter of Square =", twodfigures.square_perimeter(side))
        else:
            print("Invalid Operation")

    #User select circle
    elif choice == 2:
        radius = float(input("Enter radius of circle: "))
    #------------------------------------------
        print("1 Area")
        print("2 Circumference")
        op = int(input("Choose operation: "))
    #------------------------------------------
        #calculating operations on circle
        if op == 1:
            print("Area of Circle =", round(twodfigures.circle_area(radius), 2))
        elif op == 2:
            print("Circumference of Circle =", round(twodfigures.circle_perimeter(radius), 2))
        else:
            print("Invalid Operation")

    #User select triangle
    elif choice == 3:
        print("1 Area")
        print("2 Perimeter")
        op = int(input("Choose operation: "))
    #--------------------------------------------
        #calculating operations on triangle
        if op == 1:
            base = float(input("Enter base: "))
            height = float(input("Enter height: "))
            print("Area of Triangle =", twodfigures.triangle_area(base, height))

        elif op == 2:
            s1 = float(input("Enter side 1: "))
            s2 = float(input("Enter side 2: "))
            s3 = float(input("Enter side 3: "))
            print("Perimeter of Triangle =", twodfigures.triangle_perimeter(s1, s2, s3))
        else:
            print("Invalid Operation")

    #User select rectangle
    elif choice == 4:
        length = float(input("Enter length: "))
        breadth = float(input("Enter breadth: "))
        print("1 Area")
        print("2 Perimeter")
        op = int(input("Choose operation: "))
        #calculating operations on rectangle
        if op == 1:
            print("Area of Rectangle =", twodfigures.rectangle_area(length, breadth))
        elif op == 2:
            print("Perimeter of Rectangle =", twodfigures.rectangle_perimeter(length, breadth))
        else:
            print("Invalid Operation")

    else:
        print("Invalid Choice")