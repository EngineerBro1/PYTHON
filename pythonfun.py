# Python Functions
# A function is a block of code that performs a specific task whenever it is called. In bigger programs, where we have large amounts of code, it is advisable to create or use existing functions that make the program flow organized and neat.


# There are two types of functions:
# Built-in functions
# User-defined functions

# Built-in functions:
# These functions are defined and pre-coded in python. Some examples of built-in functions are as follows:
# min(), max(), len(), sum(), type(), range(), dict(), list(), tuple(), set(), print(), etc.

# User-defined functions:
# We can create functions to perform specific tasks as per our needs. Such functions are called user-defined functions.

# Create a function using the def keyword, followed by a function name, followed by a paranthesis (()) and a colon(:).
# Any parameters and arguments should be placed within the parentheses.
# Rules to naming function are similar to that of naming variables.
# Any statements and other code within the function should be indented
# example
# def function_name(): 
    # print("Hello")

# Calling a function:
# We call a function by giving the function name, followed by parameters (if any) in the parenthesis.
# def function_name():
#     print("Hello")
# function_name()  # calling the function

# Arguments:-
# Information can be passed into functions as arguments.
# Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.


# lets took a persons name age and country
# def person(name,age,country):
#     print(name,age,country)
# person("Rohan",34,"India")

# average of two numbers
# def avg( a,b):
#     print("The average is: ",(a+b)/2)
# avg(2,3)
    


# Default arguments:
# We can provide a default value while creating a function. This way the function assumes a default value even if a value is not provided in the function call for that argument

# average of two numbers
# def avg( a=7,b=5): # here default values are 7 and 5 which gives avg 6 whenever  no input arg given 
#     print("The average is: ",(a+b)/2)
# avg()



# Keyword arguments:
# We can provide arguments with key = value, this way the interpreter recognizes the arguments by the parameter name. Hence, the the order in which the arguments are passed does not matter.

# average of two numbers
# def avg( a=4,b=9):
#     print("The average is: ",(a+b)/2)
# avg(b = 8)




# Required arguments:
# In case we don’t pass the arguments with a key = value syntax, then it is necessary to pass the arguments in the correct positional order and the number of arguments passed should match with actual function definition


# # average of two numbers
# def avg( a,b):
#     print("The average is: ",(a+b)/2)
# avg(4,6)  # enter the args according to the required arg

# # lets took a persons name age and country
# def person(name,age,country):
#     print(name,age,country)
# person("Rohan",34,"India")
# person("Sonhan",20,"Germany")



# Number of Arguments
# By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less

# lets took a persons name age and country
# def person(name,age,country):  # here 3 args required
#     print(name,age,country)
# person("Rohan",34,"India")  # input also 3 so no error
# person("Sagar",45,"5.6ft","USA") #person() takes 3 positional arguments but 4 were given so its a error



# Variable-length arguments:
# Sometimes we may need to pass more arguments than those defined in the actual function. This can be done using variable-length arguments

# Arbitrary Arguments:
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
# This way the function will receive a tuple of arguments, and can access the items accordingly

# def average(*numbers):
#     print(type(numbers))
#     sum = 0
#     for i in numbers:
#         sum = sum+i
#     print("Average: ", sum/len(numbers))

# average(4,6,8,3,2)


# Keyword Arbitrary Arguments:
# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
# This way the function will receive a dictionary of arguments, and can access the items accordingly


# lets took a persons name age and country
# def person(**name):  
#     print("His last name is "+ name["lname"])
# person(fname="Rohan", lname = "Dash") #entering 2 args but access the required one

# return:-
# def average(*numbers):
#     sum = 0
#     for i in numbers:
#         sum = sum+i
#     # print("Average: ", sum/len(numbers))
#     return sum/len(numbers)

# a = average(4,6,8,3,2)
# print(a)

# Recursion
# Python also accepts function recursion, which means a defined function can call itself.
# Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result

# def recursion(i):
#     if (i>2):
#         result = i+recursion(i-1)
#         print(result)
#     else:
#         result = 0
#     return result
# recursion(16)
# calls and print 16 time untill con true



# pass statement
# function defination cannnot be empty i ffor some reason  the function defination remains empty to avoid he error use pass statement
# def function():
#     pass







































































