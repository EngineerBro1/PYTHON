
# In Python, access specifiers or modifiers are not used in the same explicit manner as in some other object-oriented programming languages like Java or C++. However, Python provides a convention for indicating the intended usage of attributes and methods through naming conventions and the use of underscores.
# Types of access specifiers::
# Public access modifier
# Private access modifier
# Protected access modifier

# Public: By default, all attributes and methods in Python are public, meaning they can be accessed from outside the class. Public attributes and methods are typically named without any leading underscores.

# class MyClass:
#     def __init__(self):
#         self.public_attr = 10
        
#     def public_method(self):
#         return "This is a public method"


# class Student:
#     def __init__(self):
#         self._name = "Ram"
#     def _funName(self):
#         return "Sita"
    
# class subject(Student):
#     pass
# object = Student()
# print(object._name)
# print(object._funName)



# Protected: Conventionally, attributes and methods prefixed with a single underscore (_) are considered protected, indicating that they should not be accessed directly from outside the class, but this is only a convention, and Python doesn't enforce it.


# class Student: 
#     def __init__(self, age, name): 
#         self.__age = age      
        
#         def __funName(self):  
#             self.x = 99
#             print(self.x)

# class Subject(Student):
#     pass

# obj = Student(30,"Ram")
# object= Subject
# print(obj.__age)
# print(obj.__funName())

# ??outpu:
# AttributeError: 'student' object has no attribute '__age'
# AttributeError: 'student' object has no method '__funName()'
# AttributeError: 'subject' object has no attribute '__age'
# AttributeError: 'student' object has no method '__funName()'


# Private: Conventionally, attributes and methods prefixed with double underscores (__) are considered private, meaning they should not be accessed or overridden directly from outside the class. Python performs name mangling on these names to make them less accessible, but they can still be accessed with some workarounds.

# class Student:
#     def __init__(self,age,name):
#         self.age = age
#         self.name = name
# object = Student(33,"Hari")
# print(object.age)
# print(object.name)




































































