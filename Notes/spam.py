name = "Mr. Lee"

def say_hi(name):
    print("Hello", name)

def add_two(n1, n2):
    sum = n1 + n2
    return sum

def add_multiply(n1, n2):
    sum = n1 + n2
    product = n1 * n2
    return sum, product


if __name__ == "__main__":
    say_hi("Kitty")
    x = add_two(5, 6)
    print(x)

    print(add_multiply(2, 3))
    
    sum, product = add_multiply(7,8)
    print(sum, product)