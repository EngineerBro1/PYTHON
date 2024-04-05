# Generators in Python are a convenient way to create iterators. They allow you to generate a sequence of values on-the-fly without storing the entire sequence in memory. This can be particularly useful when dealing with large datasets or infinite sequences.


# Generator Functions:
# Generator functions are defined using the def keyword, like regular functions, but they contain one or more yield statements. When called, a generator function returns a generator object, which can be iterated over using a for loop or by calling the next() function.


# def squares(n):
#     for x in range(n):
#         yield x**2

# for y in squares(10):
#     print(y)


# Generator Expressions:
# Generator expressions are similar to list comprehensions, but they use parentheses () instead of square brackets []. They also create generator objects that produce values lazily.


# cubes = (x**3 for x in range(10))
# for x in cubes:
#     print(x)



# def generator():
#     for x in range(2):
#         yield x

# gen = generator()
# print(next(gen))
# print(next(gen))





# def generator():
#     for x in range(1000000):
#         yield x
# gen = generator()
# for y in gen:
#     print(y)