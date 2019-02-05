# Formatting
import math
import random

# area of circle calculator

radius = 5
area = math.pi * radius ** 2
print(area)

#  round function
print(round(area, 2))  # round(number, precision)

for i in range(20):
    print(round(random.random(), 2))


#  format method is more useful
#  index:spaceholder+justification+sign+width+commas+precision+datatype+notation

print("My formatted number is {:.2f}".format(3.14152))
print("My formatted number is {:10}".format(3.14152))
print("My formatted number is {:10.3f}".format(3.14152))
print("My formatted number is {:<10}.".format(3.14152))
print("My formatted number is {:^10}.".format(3.14152))
print("My formatted number is ${:>10.2f}.".format(3.14152))

for i in range(20):
    print("${:<5.2f}***".format(random.random()))

for i in range(20):
    print("{:.2e}".format(random.random()))

for i in range(20):
    print("${:8,}".format(random.randrange(1000000)))

print("My formatted number is {:10d}".format(5))



















