# Recursion - function calling itself

def f():
    print("f")
    g()
def g():
    print("g")

# functions can call other functions
f()

def f():
    print("f")
    f()
    g()
def g():
    print("g")

# functions can also call themselves
#f()  # this causes a recursion error


# Controlling recursion with depth
def controlled(depth, max_depth):
    print("Recursion depth:", depth)
    if depth < max_depth:
        controlled(depth + 1, max_depth)
    print("Recursion depth", depth, "has closed")

controlled(0, 10)

# Factorial
def factorial(n):
    total = 1
    for i in range(1, n + 1):
        total *= i
    return total

print(factorial(1000))

def recursive_factorial(n):
    if n > 1:
        return n * recursive_factorial(n - 1)
    else:
        return n

print(recursive_factorial(1000))