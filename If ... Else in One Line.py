# If ... Else in One Line:
# There is also a shorthand syntax for the if-else statement that can be used when the condition being tested is simple and the code blocks to be executed are short


# a = 78
# b = 7
# print("a is greater") if a>b else print("b is greater")



# You can also have multiple else statements on the same line

# a = 7
# b = 7
# print("a is greater") if a > b else print("both are equals") if a==b else print("b is greater")





# Enumerate function in python:
# The enumerate function is a built-in function in Python that allows you to loop over a sequence (such as a list, tuple, or string) and get the index and value of each element in the sequence at the same time.

# fruits = ["apple","banana","cherry","mango"]
# for index, fruits in enumerate(fruits):
#     print(index,fruits)
#     print(f'{index}:{fruits}')


# Changing the start index:
# By default, the enumerate function starts the index at 0, but you can specify a different starting index by passing it as an argument to the enumerate function


fruits = ["apple","banana","cherry","mango"]
for index, fruits in enumerate(fruits):
    print(index+1,fruits)
    print(f'{index+1}:{fruits}')


