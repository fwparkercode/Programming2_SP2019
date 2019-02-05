def say_hi(name="Mr. Lee"):
    print("Hello", name)

def cube(n):
    return n ** 3

say_hi("Sammy")  # this will run on import
print("Blah")

if __name__ == "__main__":
    # this will not run on import
    print(cube(5))
    say_hi("Me")