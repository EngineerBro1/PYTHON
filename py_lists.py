# Python Lists
# Lists are ordered collection of data items.
# They store multiple items in a single variable.
# List items are separated by commas and enclosed within square brackets [].
# Lists are changeable meaning we can alter them after creation.
# a =[3,53,25,25,25,21,2,21,65,7,8] # this is a list (no error)
# print(a)

# List Index
# Each item/element in a list has its own unique index. This index can be used to access any particular item from the list. The first item has index [0], second item has index [1], third item has index [2] and so on.
# print(a[0]) #positive index
# print(a[:])
# print(a[:7])
# print(a[6:])
# print(a[2:8])
# print(a[-1]) #negative index
# print(a[len(a)-1]) #same as print(a[-1])

# Accessing list items
# We can access list items by using its index with the square bracket syntax [].

# Positive Indexing:
# As we have seen that list items have index, as such we can access items using these indexes.

# Negative Indexing:
# Similar to positive indexing, negative indexing is also used to access items, but from the end of the list. The last item has index [-1], second last item has index [-2], third last item has index [-3] and so on.

# Check whether an item in present in the list?
# We can check if a given item is present in the list. This is done using the in keyword.

# a =[3,53,25,25,25,21,2,21,65,7,8]
# if 25 in a:
#     print("Yes is available")
# else:
#     print("Sorry not avaliable")


# Range of Index:
# You can print a range of list items by specifying where you want to start, where do you want to end and if you want to skip elements in between the range
# a =[3,53,25,25,25,21,2,21,65,7,8]
# print(a[2:6]) # 2 is start point , 6 is the end point
# print(a[1:9:2]) # 1 is start point , 9 is end point and 2 is the skip element



# List Comprehension
# List comprehensions are used for creating new lists from other iterables like lists, tuples, dictionaries, sets, and even in arrays and strings.
# Syntax:
# List = [Expression(item) for item in iterable if Condition]
# Expression: It is the item which is being iterated.
# Iterable: It can be list, tuples, dictionaries, sets, and even in arrays and strings.
# Condition: Condition checks if the item should be added to the new list or not
# 1.
# fruits = ["apple","mango","banana","cherry","kiwi","watermelon"]
# list = []
# for x in fruits:
#     if "a" in x :
#         list.append(x)
# print(list)

# also
# fruits = ["apple","mango","banana","cherry","kiwi","watermelon"]
# list=[x for x in fruits if "a" in x]
# print(list)

# 2.
# fruits = ["apple","mango","banana","cherry","kiwi","watermelon"]
# list = [ x for x in fruits if x !="kiwi"] 
# print(list)

# 3.
# fruits = ["apple","mango","banana","cherry","kiwi","watermelon"]
# list =[x for x in fruits]
# print(list)

# 4. use range()

# list = [x for x in range(10)]
# print(list)


# 5.
# list = [ x for x in range(10) if x<7]
# print(list)


# 6. use upper case
# fruits = ["apple","mango","banana","cherry","kiwi","watermelon"]
# list = [x.upper() for x in fruits]
# print(list)

# 7.
# fruits = ["apple","mango","banana","cherry","kiwi","watermelon"]
# list = ['lichi' for x in fruits]
# print(list)


# 8.
# fruits = ["apple","mango","banana","cherry","kiwi","watermelon"]
# list = [ x if x == "banana" else "orange" for x in fruits] # except banana rest turn change into orange
# print(list)

# 9.
# fruits = ["apple","mango","banana","cherry","kiwi","watermelon"]
# list = [ x if x != "banana" else " orange" for x in fruits]
# print(list)






# List Methods
# list.sort()
# This method sorts the list in ascending order. The original list is updated
# a =[3,53,25,25,25,21,2,21,65,7,8]
# a.sort()
# print(a)

# reverse()
# This method reverses the order of the list.


# a =[3,53,25,25,25,21,2,21,65,7,8]
# a.reverse()
# print(a)


# index()
# This method returns the index of the first occurrence of the list item.

# a =[3,53,25,25,25,21,2,21,65,7,8]
# print(a.index(25))
# print(a)


# count()
# Returns the count of the number of items with the given value

# a =[3,53,25,25,25,21,2,21,65,7,8]
# print(a.count(25))
# print(a)


# copy()
# Returns copy of the list. This can be done to perform operations on the list without modifying the original list.

# a =[3,53,25,25,25,21,2,21,65,7,8]
# b = a.copy()
# b[2] = 34
# print(b)
# print(a)

# append():
# This method appends items to the end of the existing list.
# a =[3,53,25,25,25,21,2,21,65,7,8]
# a.append(0)
# print(a)

# insert():
# This method inserts an item at the given index. User has to specify index and the item to be inserted within the insert() method.
# a =[3,53,25,25,25,21,2,21,65,7,8]
# a.insert(5,0)
# print(a)


# extend():
# This method adds an entire list or any other collection datatype (set, tuple, dictionary) to the existing list.
# a =[3,53,25,25,25,21,2,21,65,7,8]
# b = [6,7,3]
# a.extend(b)
# print(a)


# Concatenating two lists: 
# You can simply concatenate two lists to join two lists.
# a =[3,53,25,25,25,21,2,21,65,7,8]
# b = [5,7,5]
# c = a+b
# print(c)

































































































