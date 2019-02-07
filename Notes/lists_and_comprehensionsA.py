#  Lists and Comprehensions

my_list = ["Abe", "Bev", "Cam", "Dan", "Eve", "Flo", "Gus"]
my_numbers = [5, 9, 12, 6, 3, -3, 4]

print(my_list[1])  # single index
print(my_list[-1])  # negative index starts at -1
print(my_list[:4])
print(my_list[-3:])
print(my_list[:])

my_copy = my_list  # NO!!!
print(my_copy)
my_copy.append("Hal")
print(my_copy)
print(my_list)

my_copy = my_list[:]  # YES!!!
print(my_copy)
my_copy.append("Ina")
print(my_copy)
print(my_list)

# 2d list
my_2dlist = [["Abe", 8], ["Bev", 5], ["Cam", 11]]
print(my_2dlist[2][0])  # Cam

# if in
if "Cam" in my_list:
    print("Cam is in there")

# list functions
print(len(my_list))  # length of the list (not the last index)
print(min(my_numbers))  # smallest number
print(min(my_list))  # smallest by alphabetical
print(max(my_numbers))
print(sum(my_numbers))

# list methods

# find the index of an item
print(my_list.index("Cam"))
my_list.append("Cam")
print(my_list.index("Cam"))  # finds only the first one.

print(my_list.count("Cam"))  # how many times does it appear
print(my_list.count("Abe"))

my_list.append("Deb")
print(my_list)
my_list.sort()  # orders the list
print(my_list)
my_numbers.sort()
print(my_numbers)

my_list.reverse()  # reverses the order
print(my_list)

# important one!  pop method
my_list.pop()  # pops one off the end of the list
print(my_list)
customer = my_list.pop()  # pops and returns the item
print(customer)
print(my_list)
customer = my_list.pop(3)  # pick which one you want to grab
print(customer)
print(my_list)

del my_list[3]
print(my_list)



