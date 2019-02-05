import random
from math import pi as my_pi  # import a single object
from random import randrange as rand
from math import *  # wildcard to import everything


print(my_import.cube(3))

if __name__ == "__main__":
    '''
    this code runs when I execute THIS file
    '''
    my_import.say_hi()
    my_cube = my_import.cube(3)
    print(my_cube)
    print(cube(random.randrange(1, 101, 2)))  # int from 1 to 100
    print(random.random())  # float from 0 to 1

    print(my_pi)
    print(rand(1, 7))
    print(cos(2))
