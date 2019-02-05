# Formatting

import random

for i in range(10):
    x = random.randrange(1, 101)
    y = random.randrange(1, 101)
    z = round(100 * x / y, 2)  # round(number, digits)

    print(z)

# format method
a = 3.987423
print("My number is: {:.3f}".format(a))

b = 897345879
print("b is: {:15}".format(b))

for i in range(20):
    c = random.randrange(10000)
    print("${:5}".format(c))

# other stuff it can do
# :spaceholder+justification+sign+width+commas?+precision+datatype+notation

for i in range(20):
    c = random.randrange(100000)
    print("{:^11}".format(c)) # justification (<, >, or ^)

for i in range(20):
    c = random.randrange(-100000, 100000)
    print("{:+}".format(c)) # sign (+, -)

for i in range(20):
    c = random.randrange(100000)
    print("{:11,}".format(c)) # commas or not

for i in range(20):
    c = random.random()  # random float from 0 to 1
    print("{:11.2f}".format(c))  # precision to 2 decimal

for i in range(20):
    c = random.randrange(100)  # random float from 0 to 1
    print("{:b}".format(c))  # represent as (f (float), d (int), b (binary)

for i in range(20):
    c = random.random()  # random float from 0 to 1
    print("{:e}".format(c))  # (% or e)

for i in range(20):
    c = random.randrange(-1000, 1000) * random.random()  # random float from 0 to 1
    print("${:>8.2f}".format(c))

for i in range(20):
    x = random.random()  # random float from 0 to 1
    y = random.randrange(1000)
    print("x is: {:.2f}\ny is: {:3}".format(x, y))  # precision to 2 decimal

for i in range(20):
    x = random.random()  # random float from 0 to 1
    y = random.randrange(1000)
    print()
    print("y is: {1:3}\nx is: {0:}\ny is: {1:2}".format(x, y))  # index to left of colon