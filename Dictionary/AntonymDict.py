"""
Level 1
Use dictionary to store antonyms of words. E.g.- 'Right':'Left', 'Up':'Down', etc. 
Display all words and then ask user to enter a word and display antonym of it.
"""

antonyms = {"Right":"Left", "Up":"Down", "Good":"Bad","Cool":"Hot"}

for i in antonyms.keys():
    print(i)

word = input("Enter Word from Above List:")

if word in antonyms.keys():
    print("Antonym of",word,"is:",antonyms[word])
else:
    print("Word Not Found....")         