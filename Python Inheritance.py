
# In Python, inheritance is a fundamental object-oriented programming (OOP) concept that allows you to create new classes (subclasses) based on existing classes (parent classes).

# 1. Base class (parent class):
# The original class from which a new class inherits attributes and methods.
# Serves as the foundation for the subclass.

# 2. Subclass (derived class, child class):
# The new class that inherits functionalities from the base class.
# Can inherit all attributes and methods from the parent class, and potentially add new ones or override existing ones.



# Syntax:

# class ParentClass:
#   # Attributes and methods of the parent class

# class Subclass(ParentClass):
#   # Additional attributes and methods specific to the subclass


# Add the __init__() Function:
# The __init__() function is called automatically every time the class is being used to create a new object.
# The child's __init__() function overrides the inheritance of the parent's __init__() function.


# Use the super() Function:

# Python also has a super() function that will make the child class inherit all the methods and properties from its parent


class Animal:
  def __init__(self, name):
    self.name = name

  def make_sound(self):
    print("Generic animal sound")

class Dog(Animal):
  def __init__(self, name, breed):
    super().__init__(name)  # Call the parent class 
    self.breed = breed

  def make_sound(self):
    print("Woof!")

# objects creating
animal1 = Animal("Fluffy")
dog1 = Dog("Buddy", "Labrador")


print(animal1.name)  
animal1.make_sound()  
print(dog1.name)  
dog1.make_sound()  
















