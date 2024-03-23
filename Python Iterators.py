# Python Iterators:
# In Python, iterators are objects that allow you to iterate over a sequence of items, one element at a time. They provide a way to efficiently access elements in a collection without loading the entire collection into memory at once. This is particularly useful for large datasets or when you only need to process elements one by one.
#  in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__()
# Using the __next__() function:
# An iterator object must define a special method called __next__(). This method retrieves the next element from the sequence and raises a StopIteration exception when there are no more elements to iterate over.
# Using the iter() function:
# The built-in iter() function takes an iterable object and returns its corresponding iterator. This allows you to create an iterator object for any iterable data structure

# Iterator: The object that implements the iterator protocol (having a __next__() method) and allows you to step through the elements one by one.
# Iterable: Any object that can be used to create an iterator. Examples include lists, tuples, strings, dictionaries (for keys), sets, and custom classes that implement the iterator protocol.


# mytuple = ("apple","banana","cherry","orange")
# myiter = iter(mytuple)
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))



# Looping Through an Iterator::
# Python's for loop leverages iterators behind the scenes. When you use a for loop on an iterable, Python internally creates an iterator object, calls __next__() to get elements one by one, and continues until the StopIteration exception is raised.

# mytuple = ("apple","banana","cherry","orange")
# for x in mytuple:
#     print(x)

# Create an Iterator::
# To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.
# As you have learned in the Python Classes/Objects chapter, all classes have a function called __init__(), which allows you to do some initializing when the object is being created.
# The __iter__() method acts similar, you can do operations (initializing etc.), but must always return the iterator object itself.
# The __next__() method also allows you to do operations, and must return the next item in the sequence.



# StopIteration::
# To prevent the iteration from going on forever, we can use the StopIteration statement.
# In the __next__() method, we can add a terminating condition to raise an error if the iteration is done a specified number of times


# --------#

# num = [1,2,3,4,5,6,7,8,9]
# myiter =  iter(num)
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# for x in num:
#     print(num)

# # example
# # Creating a custom iterator class to generate a sequence of even numbers.

# class  EvenNumbers:
#     def __init__(self,limit):
#         self.limit = limit
#         self.current = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.current< self.limit:
#             self.current+=2
#             return self.current
#         else:
#             raise StopIteration
        
# even_iter = EvenNumbers(20)
# # -----using next()---#
# # print(next(even_iter))
# # print(next(even_iter))
# #----using loop---#
# for x in even_iter:
#     print(x)




# # Creating an iterator that generates an infinite sequence of Fibonacci numbers.

class Fibonacci:
    def __init__(self):
        self.prev = 0
        self.curr = 1

    def __iter__(self):
        return self

    def __next__(self):
        result = self.prev
        self.prev, self.curr = self.curr, self.prev + self.curr
        return result

fibonacci_iter = Fibonacci()
for i in range(10):
    print(next(fibonacci_iter))  


