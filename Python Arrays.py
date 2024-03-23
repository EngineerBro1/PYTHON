
# What is an Array?
# An array is a special variable, which can hold more than one value at a time.
# If you have a list of items (a list of car names, for example)
# However, what if you want to loop through the cars and find a specific one? And what if you had not 3 cars, but 300?
# The solution is an array!


# Access the Elements of an Array:
# An array can hold many values under a single name, and you can access the values by referring to an index number.
number = [1,2,3,4,5]
# print(number[2])

# The Length of an Array:
# Use the len() method to return the length of an array
# print(len(number))

# Looping Array Elements:
# You can use the for in loop to loop through all the elements of an array
# for a in number:
#     print(a)

# Adding Array Elements:
# You can use the append() method to add an element to an array
# number.append(6)
# print(number)

# Removing Array Elements:
# You can use the pop() method to remove an element from the array
# number.pop(2)
# print(number)

# You can also use the remove() method to remove an element from the array
# number.remove(2)
# print(number)

# Array Methods
# Python has a set of built-in methods that you can use on lists/arrays.

# Method	    Description
# append()	    Adds an element at the end of the list
# clear()	    Removes all the elements from the list
# copy()	    Returns a copy of the list
# count()	    Returns the number of elements with the specified value
# extend()	    Add the elements of a list (or any iterable), to the end of the current list
# index()	    Returns the index of the first element with the specified value
# insert()	    Adds an element at the specified position
# pop() 	    Removes the element at the specified position
# remove()	    Removes the first item with the specified value
# reverse()	    Reverses the order of the list
# sort()	    Sorts the list




# /////
import array
# creat the array
num = array.array('i',[1,2,3,4,5])
# accessing
print("First element:",num[0])
print("Last element:",num[-1])
# append element to the array
num.append(6)
print("Array after appending:",num)
# Removing
num.remove(6)
print("Array after removeing:",num)
# Finding index of number
index = num.index(3)
print("Index of 3:",index)
# Inserting an element at a specific position
num.insert(3,2)
print("Array after insertion:",num)
# extending array with another array
new_num = array.array('i',[9,8,7])
num.extend(new_num)
print("Array after extention",num)
#reverse array
num.reverse()
print("Array after reversed",num)





