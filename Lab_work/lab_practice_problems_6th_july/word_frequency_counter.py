"""Problem Statement:
Accept a sentence from the user and create a dictionary that stores the frequency of each word.
Example:
Input:
python is easy and python is powerful
Output:
{
'python': 2,
'is': 2,
'easy': 1,
'and': 1,
'powerful': 1
}
Additionally:
Display the most frequently occurring words.
Display all words in alphabetical order."""
#-------------------------------Coding section-------------------------------

#Accept a sentence from the user
sentence = input("Enter a sentence: ")

#Split the sentence into words
words = sentence.split()

#Creating an empty dictionary
frequency = {}

#Count the frequency of each word
for word in words:
    if word in frequency:
        frequency[word] = frequency[word] + 1
    else:
        frequency[word] = 1

#Display the frequency of each word
print("Word Frequency:")
print(frequency)

#Find the most frequently occurring word
most_word = max(frequency, key=frequency.get)

#Display the most frequent word
print("Most Frequent Word:")
print(most_word, ":", frequency[most_word])

#Display words in alphabetical order
print("Words in Alphabetical Order:")
for word in sorted(frequency):
    print(word, ":", frequency[word])

#--------output section---------------------------#
"""Output:
Enter a sentence: python is easy and python is powerful

Word Frequency:
{'python': 2, 'is': 2, 'easy': 1, 'and': 1, 'powerful': 1}

Most Frequent Word:
python : 2

Words in Alphabetical Order:
and : 1
easy : 1
is : 2
powerful : 1
python : 2
"""