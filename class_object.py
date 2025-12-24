class dog:
# CLASS ATTRIBUTE (shared by all instances)
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # the __init__ method initializes the object's attributes ( Constructor )
    
    def bark(self):
        print(f"{self.name} says Woof!")

    def birthday(self):
        self.age += 1
        print(f"Happy Birthday {self.name}! You are now {self.age} years old.")

dog1 = dog("Buddy", 3)
dog2 = dog("Max", 5)
# Create object instances of the dog class

dog1.bark()  #Use the objects
dog2.birthday()

print(f"{dog1.name} is {dog1.age} years old")
print(f"{dog2.name} is {dog2.age} years old")

# Key terms:
# • class = Blueprint
# • __init__ = Constructor (setup method)
# • self = Refers to the current object
# • Attributes = Variables belonging to object (e.g., self.name )
# • Methods = Functions belonging to class (e.g., def bark() )