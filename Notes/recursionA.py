#  Recursion (functions calling themselves)

# Functions can call functions
def f():
    print("f")
    g()

def g():
    print("g")

f()

# Function calling itself
def f():
    print("f")
    f()

#f()

# We can control the recursion depth
def controlled(level, end_level):
    print("Recursion level:", level)
    if level < end_level:
        controlled(level + 1, end_level)
    print("Level", level, "closed")

controlled(0, 10)


