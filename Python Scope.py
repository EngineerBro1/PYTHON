# In Python, scope refers to the visibility or accessibility of variables within different parts of your code. Python has four levels of scope:
# Local Scope: Variables defined within a function have local scope. They are only accessible within that function.

# def myfun():
#     a = 20
#     print(a)
# myfun()

# Enclosing Scope (Nonlocal): Variables defined in an enclosing function can be accessed by nested functions within it using the nonlocal keyword

# def fun1():
#     a = 20

#     def fun2():
#         nonlocal a
#         a += 7
#         print(a)
#     fun2()
# fun1()



# Global Scope: Variables defined at the top level of a module or explicitly declared as global within a function have global scope. They can be accessed from anywhere in the module.


# a = 20
# def myfun():
#     print(a)

# myfun()
# print(a)

# Built-in Scope: This scope includes all the names that are preassigned in Python, such as built-in functions and exceptions.

# print(len([1,2,3,4,5,6,7,8,9,0]))



