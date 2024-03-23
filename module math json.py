# Python has a set of built-in math functions, including an extensive math module, that allows you to perform mathematical tasks on numbers.
# Built-in Math Functions:
# The min() and max() functions can be used to find the lowest or highest value in an iterable
# import math
# a = min(12,3,4)
# b = max(20,10,4)
# print(a)
# print(b)

# The abs() function returns the absolute (positive) value of the specified number
# import math
# a = abs(-4)
# print(a)

# The pow(x, y) function returns the value of x to the power of y (xy).
# import math
# a = pow(3,2)
# print(a)



# The Math Module
# Python has also a built-in module called math, which extends the list of mathematical functions.
# To use it, you must import the math module
# When you have imported the math module, you can start using methods and constants of the module.

# import math
# a = math.ceil(2.3)
# b = math.floor(2.3)
# print(a)
# print(b)

# import math
# a = math.pi
# print(a)




# Python JSON:

# Python has a built-in package called json, which can be used to work with JSON data.


# Parse JSON - Convert from JSON to Python:
# If you have a JSON string, you can parse it by using the json.loads() method.

# import json
# person = '{"name":"Ram","age":21,"Country":"India" }'
# a = json.loads(person)
# print(a["name"])

# Convert from Python to JSON:
# If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.

# import json
# person = {"name":"Ram","age":21,"Country":"India" }
# print(type(person))
# a = json.dumps(person)
# print(a)
# print(type(a))

# You can convert Python objects of the following types, into JSON strings:

# dict
# list
# tuple
# string
# int
# float
# True
# False
# None

# Python	JSON
# dict	    Object
# list  	Array
# tuple	    Array
# str 	    String
# int	    Number
# float	    Number
# True	    true
# False	    false
# None	    null

# import json
# print(json.dumps({"name":"Ram","age":21,"Country":"India" }))
# print(json.dumps([12,3,4]))
# print(json.dumps("Hi"))
# print(json.dumps(34))
# print(json.dumps(12.4))
# print(json.dumps(False))
# print(json.dumps(None))


# Format the Result:
# The json.dumps() method has parameters to make it easier to read the result
# You can also define the separators, default value is (", ", ": "), which means using a comma and a space to separate each object, and a colon and a space to separate keys from values

# import json
# person = {
#     "name":"Ram",
#     "age":45,
#     "Country":"India",
#     "bad habbits":None,
#     "Car":[
#         {"Brand":"Porche","Model":911},
#         {"Brand":"Audi","MOdel":"Q3"}
#     ]

# }
# # print(json.dumps(person,indent=3))
# print(json.dumps(person,indent=3,separators=(".","=")))

# Order the Result:
# The json.dumps() method has parameters to order the keys in the result


# import json
# person = {
#     "name":"Ram",
#     "age":45,
#     "married":True,
#     "Country":"India",
#     "bad habbits":None,
#     "Car":[
#         {"Brand":"Porche","Model":911},
#         {"Brand":"Audi","MOdel":"Q3"}
#     ]

# }
# print(json.dumps(person,indent=3,sort_keys=True))


