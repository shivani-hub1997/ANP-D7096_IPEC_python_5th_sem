"""Problem Statement
 Accept two integers representing the starting and ending values of a range.
 Display all prime numbers within the range and finally display the total number of
 prime numbers found."""

#------------coding section-------------------------------#

#taking input from the user
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

count = 0

for num in range(start, end + 1):
    if num > 1:
        is_prime = True

        for i in range(2, num):
            if num % 1 == 0:
                is_prime = Falsebreak

        if is_prime:
            print(num)
            count += 1

print("Total prime numbers:",count)