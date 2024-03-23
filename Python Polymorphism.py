# Python Polymorphism::

# The word "polymorphism" means "many forms", and in programming it refers to methods/functions/operators with the same name that can be executed on many objects or classes.
# Polymorphism is a fundamental concept in object-oriented programming (OOP) and refers to the ability of different objects to respond to the same message or method invocation in different ways. In Python, polymorphism is achieved through method overriding and method overloading.


# Method Overriding::
# Method overriding occurs when a subclass provides a specific implementation of a method that is already defined in its superclass. When you call the method on an object of the subclass, the overridden method in the subclass is executed instead of the method in the superclass.

# class Animal:
#     def  speak(self):
#         print("Animal Speaks")

# class Dog(Animal):
#     def speak(self):
#         # return super().speak()
#         print("Dog Barks")

# class Cat(Animal):
#     def speak(self):
#         # return super().speak()
#         print("Cat Meows")

# def make_sound(animal):
#     animal.speak()
# animal = Animal()
# dog = Dog()
# cat = Cat()

# make_sound(animal)
# make_sound(dog)
# make_sound(cat)



# Method Overloading::
# Python does not support method overloading in the way other languages like Java or C++ do, where multiple methods with the same name but different parameters can exist in the same class. However, you can achieve a form of method overloading by using default parameter values or variable arguments.

# class Vector:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def __add__(self,other):
#         return Vector(self.a+other.a,self.b+other.b)
#     def __str__(self):
#         return f"({self.a},{self.b})"

# Vector1 = Vector(3,4)
# Vector2 = Vector(1,2)
# print(Vector1 + Vector2)



# Function Polymorphism:
# len():
# For strings len() returns the number of characters

a = "Hello World"
print(len(a))


# For tuples len() returns the number of items in the tuple

mytuple = ("apple","banana","cherry","orange","kiwi")
print(len(mytuple))


# For dictionaries len() returns the number of key/value pairs in the dictionary

mydict = {
    "Car Brand":"Ford",
    "Model": "Mustang",
    "Year": 2021
    }
print(len(mydict))







