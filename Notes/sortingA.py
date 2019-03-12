# Sorting
import random
import time

# Swap values
a = 1
b = 2
print(a, b)

temp = a  # store it before we destroy it
a = b
b = temp
print(a, b)

# the pythonic way
a, b = b, a
print(a, b)

# make a random list of 100 numbers with value 1 to 99
# use list comprehension
rando_list = [random.randrange(1, 100) for x in range(100)]
_rando_list = rando_list[:]
#print(rando_list)

def selection_sort(my_list):
    for cur_pos in range(len(my_list)):
        min_pos = cur_pos
        for scan_pos in range(cur_pos + 1, len(my_list)):
            if my_list[scan_pos] < my_list[min_pos]:
                min_pos = scan_pos
        my_list[cur_pos], my_list[min_pos] = my_list[min_pos], my_list[cur_pos]

start_time = time.perf_counter()
selection_sort(rando_list)
print(time.perf_counter() - start_time)
#print(rando_list)


# Insertion Sort
rando_list = [random.randrange(1, 100) for x in range(100)]
#print(rando_list)

start_time = time.perf_counter()
for key_pos in range(1, len(_rando_list)):
    key_val = _rando_list[key_pos]
    scan_pos = key_pos - 1  # look to dancer on the left
    while (scan_pos >=0) and (_rando_list[scan_pos] > key_val):
        _rando_list[scan_pos + 1] = _rando_list[scan_pos]
        scan_pos -= 1

    _rando_list[scan_pos + 1] = key_val

print(time.perf_counter() - start_time)
#print(rando_list)


# Optional parameters
print("Hello", end=" ")  # end is an optional parameter with default value "\n"
print("World")

def hello(name, time_of_day="morning"):
    print("Hello", name, ", Good", time_of_day)

hello("Jim", time_of_day="evening")


# Lambda function (anonymous function on a single line)
double_me = lambda x: x * 2   # nameless function lambda parameter: return
print(double_me(5))


# Real world sorting with Python
my_list = [random.randrange(100) for x in range(10)]
print(my_list)
my_2d_list = [[random.randrange(100), random.randrange(100)] for x in range(10)]
print(my_2d_list)
name_list = ["ethan", "Benji", "lee", "Nicky", "Jonathan", "Karen", "michelle"]

# Sort method (changes the list in place)
my_list.sort()  # normal sort
my_list.sort(reverse=True)  # reverse is an optional parameter
print(my_list)

'''
def alphabetical(x):
    return x.upper()

name_list.sort(key=alphabetical)
'''
name_list.sort(key=lambda x: x.upper())
print(name_list)
name_list.sort(reverse=True, key=lambda x: len(x))
print(name_list)

my_2d_list.sort(key=lambda x: x[1])
print(my_2d_list)
my_2d_list.sort(key=lambda x: x[0] + x[1])
print(my_2d_list)
my_2d_list.sort(key=lambda x: sum(x))
print(my_2d_list)

print(sum(my_list))


# Sorted function (RETURNS a new list)
new_list = sorted(my_list, reverse=False)
print(my_list)
print(new_list)

new_list = sorted(my_list, key=lambda x: int(str(x)[-1]))  # complex example
print(new_list)