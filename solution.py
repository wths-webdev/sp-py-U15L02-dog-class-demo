# This is our dog
class Dog:
    # Constructor attributes of a Dog
    # self means the object we're creating
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # behaviors of a Dog (methods)
    def bark(self):
        print(f"{self.name} says: Woof!")

    def hasBirthday(self):
        self.age += 1


# Creating objects happens OUTSIDE of the class
# Create a dog
rosie = Dog("Rosie", 3)

# make rosie bark
rosie.bark()

# update its age
rosie.age = 15

print(rosie.age)

# what if we made a hasBirthday() method?
rosie.hasBirthday()

print(rosie.age)