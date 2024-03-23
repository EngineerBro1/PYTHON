# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.

# Syntax:
# lambda arguments : expression

# a = lambda b:b+2
# print(a(20))

# a = lambda b,c:b-c
# print(a(3,2))


# a = lambda b,c,d: b+c+d
# print(a(1,2,3))


# def fun(b):
#     return lambda a:a*b
# mul = fun(3)
# print(mul(2))

# def fun(b):
#     return lambda a:a+b
# add = fun(2)
# print(add(5))


# def fun(b):
#     return lambda a:a*b
# double = fun(2)
# tripple = fun(3)
# print(double(11))
# print(tripple(11))

# Lambda functions are often used in situations where a small function is required for a short period of time. They are commonly used as arguments to higher-order functions, such as map, filter, and reduce.





# Map, Filter and Reduce:
# map:
# The map function applies a function to each element in a sequence and returns a new sequence containing the transformed elements. 
# The map function has the following syntax::

# map(function, iterable)
# The function argument is a function that is applied to each element in the iterable argument. The iterable argument can be a list, tuple, or any other iterable object.


# a = [1,2,3,4,2,3,2,4,5,7]
# double = map(lambda b:b*2,a)
# print(list(double))


# filter:
# The filter function filters a sequence of elements based on a given predicate (a function that returns a boolean value) and returns a new sequence containing only the elements that meet the predicate
# The filter function has the following syntax::
# filter(predicate, iterable)
# The predicate argument is a function that returns a boolean value and is applied to each element in the iterable argument. The iterable argument can be a list, tuple, or any other iterable object.

# a = [1,2,3,4,2,3,2,4,5,7]
# even_num = filter(lambda b:b%2==0,a)
# print(list(even_num))



# reduce:
# The reduce function is a higher-order function that applies a function to a sequence and returns a single value.
# It is a part of the functools module in Python and has the following syntax::
# reduce(function, iterable)
# The function argument is a function that takes in two arguments and returns a single value. The iterable argument is a sequence of elements, such as a list or tuple.

# from functools import reduce
# a = [1,2,3,4,2,3,2,4,5,7]
# sum_of_num = reduce(lambda b,c:b+c,a)
# print(sum_of_num)





# 'is' vs '==' in Python::
#  In Python, is and == are both comparison operators that can be used to check if two values are equal. However, there are some important differences between the two that you should be aware of.
# The is operator compares the identity of two objects, while the == operator compares the values of the objects. This means that is will only return True if the objects being compared are the exact same object in memory, while == will return True if the objects have the same value.


# x = [9,5,6,7]
# y = [9,5,6,7]
# print(x is y)
# print(x==y)

# a = "Ram"
# b = "Ram"
# print(a==b)
# print(a is b)

# a = 2
# b = 2
# print(a == b)
# print(a is b)

