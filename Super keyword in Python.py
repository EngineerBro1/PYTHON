# In Python, the super() function is used to access methods and properties from a parent or superclass within a subclass. It provides a way to invoke methods defined in the superclass from the subclass, allowing for method overriding and inheritance.
#  It's particularly useful when you want to extend the behavior of a method in the superclass without completely replacing it.

# class  Parent:
#     def  __init__(self,name) :
#         self.name = name

#     def greet(self):
#         return f"Hello,my name is {self.name}"

# class Child(Parent):
#     def __init__(self, name,age):
#         super().__init__(name)
#         self.age = age

#     def greet(self):
#         Parent_greeting = super().greet()
#         return f"{Parent_greeting} and i am {self.age} years old"

# Child = Child("Hari",22)
# print(Child.greet())



class Base1:
    def greet(self):
        return "Hello from Base1 class"

class Base2:
    def greet(self):
        return "Hello from Base2 class"

class Child(Base1, Base2):
    def greet(self):
        parent1_greeting = super(Base1, self).greet()  # Calling method from Base1
        parent2_greeting = super(Base2, self).greet()  # Calling method from Base2
        return f"{parent1_greeting} and {parent2_greeting} from Child class"

child = Child()
print(child.greet())  # Output: Hello from Base1 class and Hello from Base2 class from Child class
