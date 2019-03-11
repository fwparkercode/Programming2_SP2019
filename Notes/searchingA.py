# Searching (Chapter 15 from programarcadegames.com)

file = open('data/super_villains.txt', 'r')  #  open file to read

print(file)


for line in file:
    print("Hello", line.strip())  # you can only read through one time

file.close()  # ends your access to file

# Open a file to write (overwrites all previous)
'''
file = open('data/super_villains.txt', 'w')  #  open file to write
file.write('Lee the Merciless\n')
file.close()

file = open('data/super_villains.txt', 'r')  #  open file to read

for line in file:
    print(line.strip())  # strip method removes any extra spaces, \t, \n

file.close()
'''
# Open a file to append (does not overwrite)
file = open('data/super_villains.txt', 'a')  # open file to append
file.write('Dan the Man\n')
file.close()

file = open('data/super_villains.txt', 'r')  #  open file to read
print()
for line in file:
    print(line.strip())  # strip method removes any extra spaces, \t, \n

file.close()

# you can make a new file by opening to write
file = open('data/oscars.txt', 'w')
file.write('Green Book\tBest Picture\n')
file.close()

# better way to open and close a file

with open('data/super_villains.txt') as f:
    for line in f:
        print(line.strip())
    read_data = f.read()  # big ol' string

# file automatically closes from with statement
print(read_data)

# Read data into a list (array)
with open('data/super_villains.txt') as f:
    villains = [x.strip().upper() for x in f]

print(villains)


# Linear Search

def linear_search(key, dictionary):
    i = 0  # index of my search

    while i < (len(dictionary) - 1) and key != dictionary[i]:
        i += 1

    if i < len(dictionary):
        return True  # Found it!
    else:
        return False # Did not find


linear_search("EDITHA THE FESTERING", villains)


# BINARY SEARCH

key = "THEODORA THE WICKED"
lower_bound = 0
upper_bound = len(villains)
found = False

# loop until we find it (or we finish the list)
while lower_bound <= upper_bound and not found:
    middle_pos = (upper_bound + lower_bound) // 2
    if villains[middle_pos] < key:
        lower_bound = middle_pos + 1
    elif villains[middle_pos] > key:
        upper_bound = middle_pos - 1
    else:
        found = True

if found:
    print(key, "was found at position", middle_pos)
else:
    print(key, "was not found after", loops, "loops")



# This function takes in a line of text and returns
# a list of words in the line.



text = "Hello, this is Alexa's phone"

import re

# This function takes in a line of text and returns
# a list of words in the line.
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)

def binary_search(key, dictionary):
    lower_bound = 0
    upper_bound = len(dictionary)
    found = False

    # loop until we find it (or we finish the list)
    while lower_bound <= upper_bound and not found:
        middle_pos = (upper_bound + lower_bound) // 2
        if villains[middle_pos] < key:
            lower_bound = middle_pos + 1
        elif villains[middle_pos] > key:
            upper_bound = middle_pos - 1
        else:
            found = True

    return found

file = open("data/AliceThroughTheLookingGlass.txt")
line_number = 0

for line in file:
    line = line.strip().upper()
    line_number += 1
    words = split_line(line)
    for word in words:
        if word.upper() == "ALICE":
            print("You found Alice on line number", line_number)


print(ord("A"))
print(chr(65))
alphabet = "AAAAABCDEFGHIJKLMNOPQRSTUVWXYZ"


new_list = list(alphabet)
print(new_list)
new_set = set(new_list)
print(new_set)
new_list = list(new_set)
print(sorted(new_list))




