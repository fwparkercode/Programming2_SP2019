# Searching (Chapter 15 on programarcadegames.com)

# open a file to read
file = open('data/villains.txt', 'r')  # default is 'r'

for line in file:
    print(line.strip())  # strip removes leading and trailing spaces, /n, /t.

file.close()  # make sure to close it

# to go through the file again, just reopen it
file = open('data/villains.txt', 'r')  # default is 'r'

for line in file:
    print("Hello", line.strip())

file.close()


# open a file to append to it.
file = open('data/villains.txt', 'a')  #  a for append

file.write("\nLee the Merciless")

file.close()

file = open('data/villains.txt')  # default is 'r'

for line in file:
    print("Hello", line.strip())

file.close()


# open and write to a file (THIS OVERWRITES YOUR FILE)

file = open('data/oscars.txt', 'w')  # if it doesn't exist, it creates one

file.write("Best Picture - Green Book\n")
file.write("Makeup - Black Panther\n")

file.close()

# easier way to open a file and read it
with open('data/villains.txt') as f:
    # we opened villains to read and assigned it a name f
    for line in f:
        print(line.strip(), end="!\n")


# To use the data, read it into a list
with open('data/villains.txt') as f:
    villain_list = [x.strip()s for x in f]

print(villain_list)




