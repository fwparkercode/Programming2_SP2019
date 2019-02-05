# Our Friend the List

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



