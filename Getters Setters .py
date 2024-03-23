# Setters :
# In Python, setters are a type of method used in object-oriented programming to set the value of attributes within a class. They are commonly used to enforce certain constraints or perform validation before assigning a value to an attribute.
# Setter methods are typically used in conjunction with property decorators to provide a way to control the assignment of values to attributes.


# //---------------------------------------------------------------------------
# class Person:
#     def __init__(self, name):
#         self._name = name

#     @property
#     def name(self):
#         return self._name

#     @name.setter
#     def name(self, value):
#         if not isinstance(value, str):
#             raise TypeError("Name must be a string")
#         self._name = value

# person = Person("Ram")
# print(person.name)  
# person.name = "Sita"
# print(person.name) 
# try:
#     person.name = 123
# except TypeError as e:
#     print(e)  

# Getters:
# In Python, getters are not explicitly defined as in some other programming languages. Instead, properties are commonly used to achieve getter-like behavior. Properties allow you to define getter and setter methods for accessing and modifying attributes of a class, respectively.


# class Person:
#     def __init__(self,name):
#         self._name =  name
#     @property
#     def name(self):
#         return self._name

# Person = Person("Ram")
# print(Person.name)






