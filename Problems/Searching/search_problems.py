'''
Complete the following 3 searching problems using techniques
from class and from Ch15 of the textbook website
'''

#1.  (6pts) Write code which finds and prints the longest
# word in the provided dictionary.  If there are more
# than one longest word, print them all.

import re
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


with open('dictionary.txt') as f:
    dictionary = [x.strip() for x in f]


print("Problem 1:")
# Strategy 1: make a word length list and find the max
word_len = [len(x) for x in dictionary]
print("The longest word is", dictionary[word_len.index(max(word_len))])

# Strategy 2: track biggest word as you go through dict
longest_word = ""
longest_len = 0

for word in dictionary:
    if len(word) > longest_len:
        longest_len = len(word)
        longest_word = word

print("The longest word is", longest_word)

# Strategy 3: lambda function (talk about today)
sorted_dictionary = sorted(dictionary, key=lambda x: len(x))
print("What sorcery is this?", sorted_dictionary[-1])



#2.  (8pts)  Write code which finds
# The total word count AND average word length
# in "AliceInWonderLand.txt"
print("\nProblem 2:")
alice_words = []

with open("AliceinWonderland.txt") as f:
    for line in f:
        words = split_line(line.strip())
        for word in words:
            alice_words.append(word)

print("Word count:", len(alice_words))
print("Avg word len:", sum([len(x) for x in alice_words]) / len(alice_words))



# CHOOSE ONE OF THE FOLLOWING TWO PROBLEMS

#3 (12pts)  How many times does "Cheshire" occur in"AliceInWonderLand.txt"?
# How many times does "Cat" occur?
# How many times does "Cheshire" immediately followed by "Cat" occur?

print("\nProblem 3:")
cheshires = 0
cats = 0
cheshire_cats = 0

for i in range(len(alice_words)):
    if alice_words[i].upper() == "CAT":
        cats +=1
    if alice_words[i].upper() == "CHESHIRE":
        cheshires +=1
        if alice_words[i + 1].upper() == "CAT":
            cheshire_cats += 1

print("Cheshire:", cheshires, "\nCat:", cats, "\nCheshire Cats:", cheshire_cats)

#### OR #####

#3  (12pts)Find the most frequently occurring
# seven letter word in "AliceInWonderLand.txt"

print("\nOr...")
# make a list containing all the 7 letter words
sevens = [x.upper() for x in alice_words if len(x) == 7]
# make a list of how many times each occur
sevens_count = [sevens.count(x) for x in sevens]
# use the max of the sevens_count to index the word
print(sevens[sevens_count.index(max(sevens_count))])



