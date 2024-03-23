# Python Dictionaries:

# Dictionary:
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# Dictionaries are written with curly brackets

# dict = {
#     "Brand": "Ford",
#     "Model": "Mustang",
#     "year": "1960"
# }
# print(dict)
# print(dict["Model"])

# Ordered or Unordered?:
# When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.
# Unordered means that the items do not have a defined order, you cannot refer to an item by using an index.


# Changeable:
# Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.
# dict = {
#     "Brand": "Ford",
#     "Model": "Mustang",
#     "year": "1960",
#     "year": "1999"
# }
# print(dict)


# dict = {
#     "Brand": "Ford",
#     "Model": "Mustang",
#     "year": "1960"
# }
# dict["color"]="Black"
# print(dict)




# Duplicates Not Allowed:
# Dictionaries cannot have two items with the same key


# Dictionary Length:
# To determine how many items a dictionary has, use the len() function

# dict = {
#     "Brand": "Ford",
#     "Model": "Mustang",
#     "year": "1960"
# }
# print(len(dict))


# Dictionary Items - Data Types:
# The values in dictionary items can be of any data type

# dict={
#     "BRAND": "Ford",
#     "ELECTRIC CAR": "False",
#     "Year": "1960",
#     "Colors": ["Black","White","Blue","Red"]
# }
# print(dict)
# print(type(dict))


# The dict() Constructor
# It is also possible to use the dict() constructor to make a dictionary.

# My_Dictionary = dict(Brand = "Ford",Year = 1960)
# print(My_Dictionary)

# Accessing Items:
# You can access the items of a dictionary by referring to its key name, inside square brackets
# There is also a method called get() that will give you the same result

# dict = {
#     "Brand": "Ford",
#     "Model": "Mustang",
#     "year": "1960"
# }
# choose = dict["Brand"]
# print(choose)
# choose = dict.get("Brand")
# print(choose)

# Get Keys:
# The keys() method will return a list of all the keys in the dictionary.
# dict = {
#     "Brand": "Ford",
#     "Model": "Mustang",
#     "year": "1960"
# }
# choose = dict.keys()
# print(choose)


# Get Values:
# The values() method will return a list of all the values in the dictionary.

# dict = {
#     "Brand": "Ford",
#     "Model": "Mustang",
#     "year": "1960"
# }
# a = dict.values()
# print(a)

# dict["color"] = "Black"
# print(a)

# Get Items:
# The items() method will return each item in a dictionary, as tuples in a list.

# dict = {
#     "Brand": "Ford",
#     "Model": "Mustang",
#     "year": "1960"
# }
# a = dict.items()
# print(a)

# dict["year"]= 1990
# print(a)

# dict["color"] = "Black"
# print(a)

# Loop Through a Dictionary:
# You can loop through a dictionary by using a for loop.
# When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well

# dict = {
#     "Brand": "Ford",
#     "Model": "Mustang",
#     "year": "1960"
# }
# if "Model" in dict:
#     print("Model is one of the key of the dictionary")




# Copy a Dictionary:
# You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.
# There are ways to make a copy, one way is to use the built-in Dictionary method copy().

# dict1 = {
#     "Brand": "Ford",
#     "Model": "Mustang",
#     "year": "1960"
# }
# # a = dict1.copy()
# # print(a)

# a = dict(dict1)
# print(a)




# Family = {
# "Member1":{
#     "Name" : "Hari",
#     "BDate": 2000
# },
# "Member2":{
#     "Name": "Ram",
#     "BDate": 2002
#     }
# }
# print(Family)



# Member1={
#     "Name" : "Hari",
#     "BDate": 2000
# }
# Member2={
#     "Name": "Ram",
#     "BDate": 2002
#     }

# Family = {
#     "Member1": Member1,
#     "Member2": Member2
# }

# print(Family)



# Dictionary Methods:
# Python has a set of built-in methods that you can use on dictionaries.

# Method	        Description
# clear()	        Removes all the elements from the dictionary
# copy()            Returns a copy of the dictionary
# fromkeys()        Returns a dictionary with the specified keys and value
# get()	            Returns the value of the specified key
# items()	        Returns a list containing a tuple for each key value pair
# keys()	        Returns a list containing the dictionary's keys
# pop()	            Removes the element with the specified key
# popitem()         Removes the last inserted key-value pair
# setdefault()      Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	        Updates the dictionary with the specified key-value pairs
# values()	        Returns a list of all the values in the dictionary














































































































