"""Problem Statement:
Write a Python program that defines a function count_vowels(text). 
The function should: 
• Accept a string.  
• Count the total number of vowels (a, e, i, o, u) irrespective of case.  
• Return the total vowel count.  
The main program should: 
• Accept a sentence from the user.  
• Call the function.  
• Display the total number of vowels.  
Sample Output 
Enter a sentence: Python Programming is Fun Total Vowels: 6  
------------------------------------------------------------------------"""

#-----------coding section---------------------------------------#
# Function to count the number of vowels in a string
def count_vowels(text):

    # Variable to store the vowel count
    count = 0

    # Traverse each character of the string
    for ch in text:

        # Convert uppercase letters to lowercase
        ch = ch.lower()

        # Check if the character is a vowel
        if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
            count += 1

    # Return the total number of vowels
    return count


# ---------------- Main Program ----------------

# Accept a sentence from the user
sentence = input("Enter a sentence: ")

# Call the function
total_vowels = count_vowels(sentence)

# Display the result
print("Total Vowels:", total_vowels)


#----------------------output section--------------------------------------


"""
Output 1
Enter a sentence: Python Programming is Fun
Total Vowels: 6

Output 2
Enter a sentence: Hello World
Total Vowels: 3

Output 3
Enter a sentence: ChatGPT is Amazing
Total Vowels: 6

Output 4
Enter a sentence: AEIOU
Total Vowels: 5

Output 5
Enter a sentence: bcdfg
Total Vowels: 0

Output 6
Enter a sentence: I Love Python
Total Vowels: 4


"""