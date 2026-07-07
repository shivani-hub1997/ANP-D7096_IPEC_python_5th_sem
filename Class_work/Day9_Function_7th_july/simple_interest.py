"""Write a program to calculate simple interest"""

#------coding section-------------------------#
#function to calculate simple interest
def calculate_simple_interest(principal,rate,time):
    return(principal*rate*time)/100
#----------------------------------------------
#main program
principal = float(input("Enter principal(in Rs): "))
rate = float(input("Enter rate(in %): "))
time = int(input("Enter time(in year): "))
print("Simple interest:Rs", calculate_simple_interest(principal,rate,time))


#-------output section-------------------------#
"""Output:
Enter principal(in Rs): 4000
Enter rate(in %): 7.6
Enter time(in year): 3 
Simple interest:Rs 912.0
-----------------------------------------------"""