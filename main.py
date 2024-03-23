#->Programming is a way for us to tell computers what to do and it only does what we tell it to do.
#
###-->What is Python?
#Python is a dynamically typed, general purpose programming language that supports an object-oriented programming approach as well as a functional programming approach.
#Python is an interpreted and a high-level programming language.
#It was created by Guido Van Rossum in 1989.

#-->Features of Python
#Python is simple and easy to understand.
#It is Interpreted and platform-independent which makes debugging very easy.
#Python is an open-source programming language.
#Python provides very big library support. Some of the popular libraries include NumPy, Tensorflow, Selenium, OpenCV, etc.

#-->What is Python used for
#Python is used in Data Visualization to create plots and graphical representations.
#Python helps in Data Analytics to analyze and understand raw data for insights and trends.
#It is used in AI and Machine Learning to simulate human behavior and to learn from past data without hard coding.
#It is used to create web applications.
#It can be used to handle databases.
#It is used in business and accounting to perform complex mathematical operations along with quantitative and qualitative analysis.

##our first program
# print("Hello world")
# print("876")

#-->MODULE
#Module is like a code library which can be used to borrow code written by somebody else in our python program. There are two types of modules in python.
#Built in Modules - These modules are ready to import and use and ships with the python interpreter. there is no need to install such modules explicitly.
#External Modules - These modules are imported from a third party file or can be installed using a package manager like pip or conda. Since this code is written by someone else, we can install different versions of a same module with time.




# Python Comments
# A comment is a part of the coding file that the programmer does not want to execute, rather the programmer uses it to either explain a block of code or to avoid the execution of a specific part of code while testing.
# To write a comment just add a ‘#’ at the start of the line.

#print("Hello World")




# Escape Sequence Characters
# To insert characters that cannot be directly used in a string, we use an escape sequence character.

# An escape sequence character is a backslash \ followed by the character you want to insert.

# An example of a character that cannot be directly used in a string is a double quote inside a string that is surrounded by double quotes:

# print("Hello\"World")
# print(5,6,7,8,9,sep="-",end="000")

# What is a variable?
# Variable is like a container that holds data. Very similar to how our containers in kitchen holds sugar, salt etc Creating a variable is like creating a placeholder in memory and assigning it some value

# What is a Data Type?
# Data type specifies the type of value a variable holds. This is required in programming to do various operations without causing an error.
# In python, we can print the type of any operator using type function
# a=67
# b=67.4
# c="Hello"
# d=complex(4,5)
# print(a)
# print(b)
# print(d)


#check data type of the variable a 
# print(type(a))#int type data
# print(type(b))
# print(type(c))
# print(type(d))


# 1. Numeric data: int, float, complex
# int: 3, -8, 0
# float: 7.349, -9.0, 0.0000001
# complex: 6 + 2i
# 2. Text data: str
# str: "Hello World!!!", "Python Programming"

# 3. Boolean data:
# Boolean data consists of values True or False.
# e=True
# print(type(e))
# 4. Sequenced data: list, tuple
# list: A list is an ordered collection of data with elements separated by a comma and enclosed within square brackets. Lists are mutable and can be modified after creation.
# list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]
# print(list1)
# Tuple: A tuple is an ordered collection of data with elements separated by a comma and enclosed within parentheses. Tuples are immutable and can not be modified after creation.
# tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"))
# print(tuple1)

# dict: A dictionary is an unordered collection of data containing a key:value pair. The key:value pairs are enclosed within curly brackets.
# dict1 = {"name":"Sakshi", "age":20, "canVote":True}
# print(dict1)


# Operators:
# Python has different types of operators for different operations. To create a calculator we require arithmetic operators.

# Arithmetic operators:
# Operator	Operator Name	Example
# +	    Addition	
# -	    Subtraction	
# * 	Multiplication	
# **	Exponential	
# / 	Division	
# %	    Modulus	
# //	Floor Division	
# a=15
# b=3
# print(a+b)
# print(a-b)
# print(a*b)
# print(a**b)
# print(a/b)
# print(a%b)# 15 divisible by 3 and give 0 remder
# print(a//b)


# Typecasting in python:-
# The conversion of one data type into the other data type is known as type casting in python or type conversion in python.

# Python supports a wide variety of functions or methods like: int(), float(), str(), ord(), hex(), oct(), tuple(), set(), list(), dict(), etc. for the type casting in python.

# a= "45"
# b="56"
# print(int(a)+int(b))  # It is Explixit Type casting

# Two Types of Typecasting:-
# Explicit Conversion (Explicit type casting in python)
# Implicit Conversion (Implicit type casting in python).
# Explicit typecasting:
# The conversion of one data type into another data type, done via developer or programmer's intervention or manually as per the requirement, is known as explicit type conversion.

# It can be achieved with the help of Python’s built-in type conversion functions such as int(), float(), hex(), oct(), str(), etc .



# Implicit Conversion
# While performing any operations on variables with different data types in Python, one of the variable's data types will be changed to the higher data type. According to the level, one data type is converted into other by the Python interpreter itself (automatically). This is called, implicit typecasting in python.

# Python converts a smaller data type to a higher data type to prevent data loss
# a=7.8
# b=354
# print(a+b)#converted into higher datatype float



# Taking User Input in python
# In python, we can take user input directly by using input() function.This input function gives a return value as string/character hence we have to pass that into a variable
# But input function returns the value as string. Hence we have to typecast them whenever required to another datatype.
#

# value1 = int(input("Enter the value: "))
# print(value1)
# print(type(value1))
# value2 = int(input("Enter the Second Value: "))
# print(value2)
# print(type(value2))
# print(value1+value2)


# What are strings?
# In python, anything that you enclose between single or double quotation marks is considered a string. A string is essentially a sequence or array of textual data. Strings are used when working with Unicode characters.
# 
# Name = input("Enter Your Name: ")
# print(Name)
# print(type(Name))
# 
# This is single line string
# Name = "Dhoni"
# print(Name)
# print(type(Name))

# Multiline string 
# a = """Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua"""
# print(a)
# print(type(a))





# Accessing Characters of a String
# In Python, string is like an array of characters. We can access parts of string by using its index which starts from 0.
# Square brackets can be used to access elements of the string

# Name = "Dhoni"
# print(Name[1])
# print(type(Name))

# Lets use a For loop for characters
# Name = "Dhoni"
# for character in Name:
#     print(character)












































