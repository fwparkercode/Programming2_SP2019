# A review of Classes

# TO DO LIST:
# make a Person class
# create an instance of Person class
# give the object attributes
# change the attributes using dot notation
# use a constructor to assign attributes
# make other methods
# make a child class (show inheritance)

class Person():
    # class attributes
    age = 0
    name = "Doe"
    apples = 2

    def __init__(self, name):
        # automatically runs when you create a new instance
        self.name = name
        print("A new person named", name, "has been added!")
    def say_hi(self):
        print(self.name, "says Hi!")

class Student(Person):
    def give_apple(self, teacher):
        if self.apples > 0:
            self.apples -= 1
            teacher.apples += 1
            print(self.name, "gives an apple to", teacher.name)

class Teacher(Person):
    def __init__(self, name):
        super().__init__(name)
        self.apples = 0
        print("A new teacher has been added")
    def eat_apple(self):
        if self.apples > 0:
            print(self.name, "ate an apple.  Yum!")
            self.apples -= 1

person1 = Person("Ava")  # creates instance of the class
person1.age = 10  # changes attribute using dot notation
print(person1.age)  # attribute of the instance
print(Person.age)  # attribute of the class
person1.x = 100  # making a new attribute
print(person1.x)
person1.say_hi()

person2 = Student("Bob")
person2.say_hi()  # person2 inherited all methods from Person class
print(person2.age)

person3 = Teacher("Cal")
print(person3.name)
person3.say_hi()

person2.give_apple(person3)
person2.give_apple(person3)

print(person3.apples)



