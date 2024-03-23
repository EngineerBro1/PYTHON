# Introduction to Object-Oriented Programming in Python: In programming languages, mainly there are two approaches that are used to write program or code.
# 1). Procedural Programming
# 2). Object-Oriented Programming

# Procedural Programming:
# In Python, procedural programming is a way of organizing code by breaking it down into a series of procedures, also known as functions. These functions are essentially self-contained blocks of code that perform specific tasks, taking inputs (parameters) and returning outputs (values) if needed.


#  The program is structured around functions that perform specific tasks.
#  The program is written in a top-down manner, starting with the overall functionality and then breaking it down into smaller, more manageable functions.
# This approach is generally easier to grasp for beginners who are starting to learn programming.
# It can be efficient for smaller projects where complex object interactions are not required.
# Functions promote reusability and modularity, making the code easier to maintain and understand.


# Object-Oriented Programming::
# Python Classes: 
# A class serves as a template or blueprint for creating objects. It defines the structure and behavior of a particular type of object.
# A class specifies the attributes (data) that objects of that type will possess, and the methods (functions) that objects of that type can perform.
# Create a Class:
# To create a class, use the keyword "class"
# class myclass:
#     a = 3
# print(myclass)



# Python Objects:
# An object is an instance of a class, representing a specific entity with its own set of attributes.
# Each object created from a class has its own unique data values for the defined attributes. They can also call the methods defined in the class to perform actions.

# Create Object:
# Now we can use the class named MyClass to create objects
# class myclass:
#     a = 12
# object = myclass()
# print(object.a)


# The __init__() Function:
# The __init__() function, also known as the constructor, is a special method in Python classes that is called automatically whenever you create a new object of that class. It is used to initialize the object's attributes (data) with starting values.
# Purpose::
# Initializes attributes of a newly created object.
# Sets up the initial state of the object.
# Provides a way to customize object behavior during creation.
# # Syntax::
# def __init__(self, parameter1, parameter2, ...):
#   """
#   This docstring explains the purpose of the constructor.
#   """
#   self.attribute1 = parameter1
#   self.attribute2 = parameter2
#   # ... assign values to other attributes using parameters



# class person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
# object = person("John",22)
# print(object.name)
# print(object.age)


# class person:
#     name = "Ram"
#     age = 22

#     def desc(self):
#         print("My name is",self.name,"and i'm",self.age,"years old")
# object = person()
# object.desc()











