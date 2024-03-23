# Tuple:
# Tuples are used to store multiple items in a single variable.
# Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets
# example: 
# A_tuple = ("apple","banana","cherrry","kiwi")
# print(type(A_tuple))

# Tuple Items:
# Tuple items are ordered, unchangeable, and allow duplicate values.
# Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
# Ordered:
# When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
# Unchangeable:
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
# Allow Duplicates:
# Since tuples are indexed, they can have items with the same value
# example 
# A_tuple = ("apple","banana","cherrry","kiwi","banana","apple")
# print(A_tuple)


# Tuple Length:
# To determine how many items a tuple has, use the len() function
# A_tuple = ("apple","banana","cherrry","kiwi")
# print(len(A_tuple))


# Create Tuple With One Item:
# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
# a = ("banana",) # this cannot recognize it as tuple so add a comma after  bananan so it consider as tuple
# print(type(a) )


# Tuple Items - Data Types:
# Tuple items can be of any data type
# A tuple can contain different data types
#  data type like = str , float , int , bool
# A_tuple = ("apple",23,45.2,True)

# Access Tuple Items:
# You can access tuple items by referring to the index number, inside square brackets
# A_tuple = ("apple","banana","cherrry","kiwi")
# print(A_tuple[0])
# print(A_tuple[3])

# Negative Indexing:
# Negative indexing means start from the end.
# -1 refers to the last item, -2 refers to the second last item etc
# A_tuple = ("apple","banana","cherrry","kiwi")
# print(A_tuple[-1])
# print(A_tuple[len(A_tuple)-2]) # 4-2 = 2


# Range of Indexes:
# You can specify a range of indexes by specifying where to start and where to end the range.
# When specifying a range, the return value will be a new tuple with the specified items
# A_tuple = ("apple","banana","cherrry","kiwi")
# print(A_tuple[1:3])

# Range of Negative Indexes:
# Specify negative indexes if you want to start the search from the end of the tuple
# A_tuple = ("apple","banana","cherrry","kiwi")
# print(A_tuple[-4:-1])


# Check if Item Exists
# To determine if a specified item is present in a tuple use the in keyword
# A_tuple = ("apple","banana","cherrry","kiwi")
# if "Mango" in A_tuple:
#     print("Yes, this fruit is available ")
# else:
#     print("Sorry this fruit is not available ")

# Change Tuple Values:
# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
# A_tuple = ("apple","banana","cherrry","kiwi")
# b = list(A_tuple)
# b[0] = "orange"
# A_tuple = tuple(b)
# print(A_tuple)


# Add Items:
# Since tuples are immutable, they do not have a built-in append() method, but there are other ways to add items to a tuple.
# 1. Convert into a list: Just like the workaround for changing a tuple, you can convert it into a list, add your item(s), and convert it back into a tuple
# A_tuple = ("apple","banana","cherrry","kiwi")
# b = list(A_tuple)
# b[0] = "orange"
# A_tuple = tuple(b)
# print(A_tuple)

# 2. Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple
# A_tuple = ("apple","banana","cherrry","kiwi")
# B_tuple = ("orange",)
# A_tuple += B_tuple
# print(A_tuple)



# Remove Items:
# Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround as we used for changing and adding tuple items
# A_tuple = ("apple","banana","cherry","kiwi")
# b = list(A_tuple)
# b.remove("cherry")
# A_tuple = tuple(b)
# print(A_tuple)


# Or you can delete the tuple completely
# A_tuple = ("apple","banana","cherry","kiwi")
# del A_tuple
# print(A_tuple) # it shows error due the tuple is totally deleted 



# Unpacking a Tuple:
# When we create a tuple, we normally assign values to it. This is called "packing" a tuple
# A_tuple = ("apple","banana","cherry","kiwi") # this is a packing tuple

# But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking"
# A_tuple = ("apple","banana","cherry")
# (Red , Yellow , Red) = A_tuple
# print(Red)
# print(Yellow)
# print(Red)

# Using Asterisk*
# If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list
# A_tuple = ("apple","banana","cherry","kiwi")
# ( *Red,Yellow ) = A_tuple

# print(Yellow)
# print(Red)

# If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left
# A_tuple = ("apple","banana","cherry","kiwi","orange")
# (Red , *Yellow , Red) = A_tuple
# print(Red)
# print(Yellow)
# print(Red)


# Loop Through a Tuple:
# You can loop through the tuple items by using a for loop.
# A_tuple = ("apple","banana","cherry","kiwi")
# for x in A_tuple:
#     print(x)


# Loop Through the Index Numbers:
# You can also loop through the tuple items by referring to their index number.
# Use the range() and len() functions to create a suitable iterable

# A_tuple = ("apple","banana","cherry","kiwi")
# for i in range (len(A_tuple)):
#     print(A_tuple[i])



# Using a While Loop:
# You can loop through the tuple items by using a while loop.
# Use the len() function to determine the length of the tuple, then start at 0 and loop your way through the tuple items by referring to their indexes.
# Remember to increase the index by 1 after each iteration

# A_tuple = ("apple","banana","cherry","kiwi")
# i = 0 
# while i < len(A_tuple):
#     print(A_tuple[i])
#     i +=1



# Join Two Tuples:
# To join two or more tuples you can use the + operator
# A_tuple = ("apple","banana","cherry","kiwi")
# num = (1,2,3)
# New_tuple = A_tuple + num
# print(New_tuple)


# Multiply Tuples:
# If you want to multiply the content of a tuple a given number of times, you can use the * operator
# A_tuple = ("apple","banana","cherry","kiwi")
# New_tuple = A_tuple * 4
# print(A_tuple)
# print(New_tuple)
























































































































































































# Python Tuples
# Tuples are ordered collection of data items. They store multiple items in a single variable. Tuple items are separated by commas and enclosed within round brackets ().




# Tuple Indexes
# Each item/element in a tuple has its own unique index. This index can be used to access any particular item from the tuple. The first item has index [0], second item has index [1], third item has index [2] and so on.


# Accessing tuple items:
# I. Positive Indexing:
# As we have seen that tuple items have index, as such we can access items using these indexes.


# II. Negative Indexing:
# Similar to positive indexing, negative indexing is also used to access items, but from the end of the tuple. The last item has index [-1], second last item has index [-2], third last item has index [-3] and so on


# III. Check for item:
# We can check if a given item is present in the tuple. This is done using the in keyword.


# IV. Range of Index:
# You can print a range of tuple items by specifying where do you want to start, where do you want to end and if you want to skip elements in between the range.



# Manipulating Tuples
# Tuples are immutable, hence if you want to add, remove or change tuple items, then first you must convert the tuple to a list. Then perform operation on that list and convert it back to tuple.






# Tuple methods
# As tuple is immutable type of collection of elements it have limited built in methods.They are explained below
# count() Method
# The count() method of Tuple returns the number of times the given element appears in the tuple.


# index() method
# The Index() method returns the first occurrence of the given element from the tuple.


# index() method
# The Index() method returns the first occurrence of the given element from the tuple.



















































































