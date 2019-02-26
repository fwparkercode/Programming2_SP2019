# Our Friend the List
import random

my_list = ["Bev", "Abe", "Cam", "Dan", "Eve", "Flo", "Gus"]
my_nums = [8, 4, 7, 5, 2, 19]

print(my_list[1])  # print Abe
print(my_list[4:]) # print Eve Flo Gus
print(my_list[:3])
print(my_list[2:4])
print(my_list[-2])

# copy of a list
#my_list2 = my_list # don't do this!!!
my_list2 = my_list[:]  # do it this way !!!!
my_list2.append("Hal")
print(my_list2)
print(my_list)

# if in
if "Cam" in my_list:
    print("Cam is in there")

# 2d list
my_list2d = [["Bev", 8], ["Abe", 12] , ["Cam", 4]]
print(my_list2d[1][0])  # print Abe
print(my_list2d[-1])  # last item in list

#  Some list functions
print(min(my_nums))
print(max(my_nums))
print(sum(my_nums))

#  Some list methods
my_list.append("Hal")
print(my_list)
print(my_list.count("Abe"))
my_list.append("Abe")
print(my_list.count("Abe"))
my_list.insert(3, "Deb")
print(my_list)

my_list.sort()
print(my_list)
my_list.append("erv")
print(my_list)
my_list.sort()
print(my_list)

my_list.reverse()
print(my_list)

# Important ones
name = my_list.pop()  # returns the popped item
print(my_list)
print(name)

my_list.pop(0)
print(my_list)

# deleting items
del my_list[4]
print(my_list)


# finding the index of an item.
print(my_list.index("Dan"))   # gives index of first item found



# ITERATION

my_list = []

for i in range(10):
    my_list.append(i)

print(my_list)

# for each loop
for num in my_list:
    num += 10  # num is just a copy, does not change the list
    print(num)
print(my_list)


# add 10 to each item in my list (using index variable loop)
for i in range(len(my_list)):
    my_list[i] += 10
print(my_list)


# make a 2d list that is 10 x 10 [[0,0], [0,1], [0,2]...[9,9]]
my_list = []
for i in range(10):
    for j in range(10):
        my_list.append([i, j])
print(my_list)


#  print each pair in the list
for pair in my_list:
    print(pair[0], pair[1])

# add 10 to each item
for i in range(len(my_list)):
    for j in range(len(my_list[i])):
        my_list[i][j] += 10

print(my_list)

# LIST COMPREHENSION
# Syntactic Sugar
# [returned_item for iterator in range/list filter]

# make a list from 0 to 100
my_list = [x for x in range(100)]
print(my_list)

# make a list of squares from 0 to 100
my_list = [x ** 2 for x in range(101)]
print(my_list)

# make a list of squares from 0 to 100, but only odd ones
my_list = [x ** 2 for x in range(100) if x ** 2 % 2 == 1]
print(my_list)

# make a list of 100 random numbers from 1 to 100
my_list = [random.randrange(1, 101) for x in range(100)]
print(my_list)

# we can also go back through lists to make a NEW list
my_list2 = [x for x in my_list if x > 50]
print(my_list2)

# roll two dice 100 times and put in list
my_list = [[random.randrange(1, 7), random.randrange(1, 7)] for x in range(100)]
print(my_list)

# roll two dice 100 times and only keep the 7s
my_list = [x for x in [[random.randrange(1, 7), random.randrange(1, 7)] for x in range(100)] if x[0] + x[1] == 7]
print(my_list)


values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
suits = ["H", "D", "C", "S"]

deck = []
for value in values:
    for suit in suits:
        deck.append(value + suit)  # concatenation
print(deck)

# list concatenation
print(values + suits)

# Strings using indices
first = "Aaron"
last = "Lee"
print(first + " " + last)
print(first[0])
print(first[-2:])
for char in first:
    print(char)
print(len(first))
if "L" in last:
    print("Yep")

print(first.upper())

print('''
   You
can
         print
  this

 :)
''')

print("Hello", end=" ")
print("World")

name = input("What is your name? ")
print("Hello", name)








