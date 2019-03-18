# Exceptions (short topic)

try:
    val = int(input("Enter a number: "))
except:
    print("You entered an invalid number")


# a better way to write it (keep asking until it works)
done = False
while not done:
    try:
        val = int(input("Enter a number: "))
        done = True
    except:
        print("You entered an invalid number")

# Error Types

# Value Error
try:
    int("a")  # this line throws a value error
except ValueError:
    print("Value Error")

# Divide by zero
try:
    val = 3 / 0  # this produces a dived by zero error
except ZeroDivisionError:
    print("ZeroDivisionError")

# Input Output error
try:
    my_file = open("my_file.txt")  # produces FileNOtFoundError
except FileNotFoundError:
    print("File not found")

# Catch multiple errors
try:
    #y = 10 / 0
    int("A")
except Exception as e:
    print("Exception caught")
    print(e)


# Make an MPG calculator

done = False
while not done:
    try:
        miles = float(input("Miles traveled: "))
        gallons = float(input("Gallons used: "))
        done = True
    except:
        print("You entered an invalid number.")

try:
    print("Your MPG: {:.2f}".format(miles / gallons))
except:
    print("Your MPG is infinite.")

# finally (always runs regardless of error or not)
try:
    my_file = open('my_file.txt', 'w')
    f = my_file.write("Hi")
except NameError:
    print("I/O error")
finally:
    my_file.close()


