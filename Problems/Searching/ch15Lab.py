'''
Complete the chapter lab at http://programarcadegames.com/index.php?chapter=lab_spell_check
'''

import re


# This function takes in a line of text and returns
# a list of words in the line.


file = open("data/AliceThroughTheLookingGlass.txt")
line_number = 1

for line in file:
    line = line.strip().upper()
    line_number += 1
    words = split_line(line)
    for word in words:
        if word.upper() == "Alice":
            print("You found Alice on line number", line_number)