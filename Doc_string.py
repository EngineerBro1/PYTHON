# Docstrings in python:
# Python docstrings are the string literals that appear right after the definition of a function, method, class, or module.
# Example Lets findout square of a number
# def square(n):
#     '''Here the given number is n , we go square of n'''
#     print(n**2)
# square(5)
# print(square.__doc__)

# Lets take input from user
# def square(n):
#     '''Here we take number from the user and got square of n'''
#     print(int(n)**2)
# square(input("Enter a number: "))



# Python Comments vs Docstrings
# Python Comments
# Comments are descriptions that help programmers better understand the intent and functionality of the program. They are completely ignored by the Python interpreter.

# Python docstrings
# As mentioned above, Python docstrings are strings used right after the definition of a function, method, class, or module . They are used to document our code.
# We can access these docstrings using the doc attribute.

# Python doc attribute
# Whenever string literals are present just after the definition of a function, module, class or method, they are associated with the object as their doc attribute. We can later use this attribute to retrieve this docstring.

# # Example Lets findout square of a number
# def square(n):
#     '''Here the given number is n , we go square of n'''
#     return n**2
# square(5)
# print(square.__doc__)







# PEP 8
# PEP 8 is a document that provides guidelines and best practices on how to write Python code. It was written in 2001 by Guido van Rossum, Barry Warsaw, and Nick Coghlan. The primary focus of PEP 8 is to improve the readability and consistency of Python code.
# PEP stands for Python Enhancement Proposal, and there are several of them. A PEP is a document that describes new features proposed for Python and documents aspects of Python, like design and style, for the community.


# Python Recursive Function
# In Python, we know that a function can call other functions. It is even possible for the function to call itself. These types of construct are termed as recursive functions
# Example of recursion in this we call the function factorial and finding ans..
# Example Lets findout factorial of  a number
# a = input("Enter a number you want to findout Factorial: ")
# def factorial(a):
#     if (a == 1 or a == 0):
#         return 1
#     else:
#         return (int(a)*factorial(int(a)-1))
# print("Number:",a)
# print("Factorial: ",factorial(a))

# witho out taking user input
# def factorial(a):
#     if (a == 1 or a == 0):
#         return 1
#     else:
#         return (a*factorial(a-1))
# a = 5;    
# print("Number : ",a)
# print("Factorial: ",factorial(a))










































