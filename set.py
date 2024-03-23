# Python Sets:
# Set:
# Sets are used to store multiple items in a single variable.
# Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
# A set is a collection which is unordered, unchangeable
#  Set items are unchangeable, but you can remove items and add new items.
# Sets are written with curly brackets

# set = {"apple","banana","cherry","orange"}
# print(set)
# print(type(set))

# Set Items:
# Set items are unordered, unchangeable, and do not allow duplicate values
# Unordered:
# Unordered means that the items in a set do not have a defined order.
# Set items can appear in a different order every time you use them, and cannot be referred to by index or key.
# Unchangeable:
# Set items are unchangeable, meaning that we cannot change the items after the set has been created.
# Once a set is created, you cannot change its items, but you can remove items and add new items.
# Duplicates Not Allowed:
# Sets cannot have two items with the same value.
# Example::
# duplicate value nott allowed
# set = {1,3,1,4}
# print(set)

# True and 1 are same in set
# set = {4,2,True,1,False} #First True comes so it print True and ignore 1
# print(set)
# set = {1,True,3} #Here first 1 comes so 1 is printed and ignore True
# print(set)


# # False and  0 are consider as same
# set = {0,2,False}
# print(set)
# set1 = {False,4,542,0}
# print(set1)


# Get the Length of a Set:
# To determine how many items a set has, use the len() function.
# set = {1,3,4,452,34}
# print(len(set))

# Set Items - Data Types
# # Set items can be of any data type
# set1 = {"apple","banana","cucumber"}  #it is a string type set
# set2 = {1,3,345}  #it is a int type set
# set3 = {True,False} #it is a boolean type set


# A set can contain different data types
# set = {"apple",2,True} # a set can contain different data type values

# type():
# From Python's perspective, sets are defined as objects with the data type 'set'

# set = {"apple","banana","cherry","orange"}
# print(type(set))


# The set() Constructor:
# It is also possible to use the set() constructor to make a set.

# set = set((1,3,4))
# print(set)

# Access Items:
# You cannot access items in a set by referring to an index or a key.
# But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.

# set = {"apple","banana","cucumber","papaya","orange"}
# # for x in set:
# #     print(x)

# print("banana" in set)  # checking if the item present or not




# Add Items:
# Once a set is created, you cannot change its items, but you can add new items.
# To add one item to a set use the add() method.
# set = {1,4,4,5}
# set.add(7)
# print(set)


# Add Sets:
# To add items from another set into the current set, use the update() method.
# set = {2,5}
# set1 = {6,8}
# set.update(set1)
# print(set)  #its automatically in asending order

# Add Any Iterable:
# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).

# set = {3,4}
# list = [6.7,8]
# set.update(list)
# print(set)




# Remove Item:
# To remove an item in a set, use the remove(), or the discard() method.


# You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.
# set = {1,2,3,4,5,6,7,8,9,0}
# set.remove(5)
# print(set)
# set.discard(4)
# print(set)
# set.pop()
# print(set)
# set.clear()
# print(set)
# del set
# print(set)


# Loop Items/:
# You can loop through the set items by using a for loop

# set = {"apple","banana","cucumber","papaya","orange"}
# for x in set:
#     print(x)


# Join Two Sets:
# There are several ways to join two or more sets in Python.
# You can use the union() method that returns a new set containing all items from both sets, or the update() method that inserts all the items from one set into another

# set = {1,2,3}
# set1 = {4,5,6}
# set2 = set.union(set1)
# print(set2)

# set.update(set1)
# print(set)


# Keep ONLY the Duplicates/:
# The intersection_update() method will keep only the items that are present in both sets.


# set = {1,2,3}
# set1 = {3,4,5,6}
# set.intersection_update(set1)
# print(set)




# The intersection() method will return a new set, that only contains the items that are present in both sets


# set = {1,2,3}
# set1 = {3,4,5,6}
# set2 = set.intersection(set1)
# print(set2)



# Keep All, But NOT the Duplicates:
# The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.


# set = {1,2,3}
# set1 = {3,4,5,6}
# # set.symmetric_difference_update(set1)
# # print(set)

# set2 = set.symmetric_difference(set1)
# print(set2)

# Set Methods:
# Python has a set of built-in methods that you can use on sets.

# Method	                        Description
# add()	                            Adds an element to the set
# clear()           	            Removes all the elements from the set
# copy()	                        Returns a copy of the set
# difference()	                    Returns a set containing the difference between two or more sets
# difference_update()	            Removes the items in this set that are also included in another, specified set
# discard()	                        Remove the specified item
# intersection()	                Returns a set, that is the intersection of two other sets
# intersection_update()	            Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	                    Returns whether two sets have a intersection or not
# issubset()	                    Returns whether another set contains this set or not
# issuperset()	                    Returns whether this set contains another set or not
# pop()	                            Removes an element from the set
# remove()	                        Removes the specified element
# symmetric_difference()	        Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	    inserts the symmetric differences from this set and another
# union()	                        Return a set containing the union of sets
# update()	                        Update the set with the union of this set and others




























































































