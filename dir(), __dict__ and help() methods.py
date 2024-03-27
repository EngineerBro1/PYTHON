# dir(), __dict__ and help() methods in python:

# dir():
# The dir() function returns a list of valid attributes for the specified object.
# When called without arguments, it returns a list of names in the current local scope.
# When called with an object as an argument, it returns a list of valid attributes for that object, including both the names of attributes and methods.
# It's a powerful tool for exploring the structure and capabilities of objects, modules, and classes.

# class Myclass:
#     def __init__(self,a) :
#         self.a = a

# print(dir())
# print(dir(Myclass))



# __dict__:
# The __dict__ attribute is a dictionary containing the namespace of the object.
# For classes, it contains the attributes and methods of the class.
# For instances of classes, it contains the instance variables and their values.
# It's useful for examining the internal state of objects and classes.

# class Myclass:
#     class_var = "class_variable"

#     def __init__(self,a) :
#         self.instance_var = a

# object = Myclass(20)
# print(object.__dict__)
# print(Myclass.__dict__)


# help():
# The help() function provides documentation and information about objects, modules, functions, classes, etc.
# When called without arguments, it starts an interactive help session.
# When called with an object, function, or module as an argument, it prints its documentation string (docstring) if available.
# It's a valuable tool for understanding how to use and interact with various parts of the Python language.

# help(dir)



