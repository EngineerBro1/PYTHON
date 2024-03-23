# What are Python Class Methods?
# In Python, class methods are methods within a class that are bound to the class itself rather than to instances of the class. They are defined using the @classmethod decorator and receive the class itself as the first parameter, conventionally named cls.

# # Why Use Python Class Methods?
# Alternative Constructors: Class methods provide a way to define alternative constructors for a class. This allows you to create instances of the class using different initialization parameters or formats. For example, you might have a class method that parses data from a string and returns an instance of the class.
# Accessing Class-Level Variables: Class methods have access to class-level variables and attributes. This makes them useful for performing operations that involve class-wide state or configuration. For example, you can use class methods to modify class variables or access class constants.
# Factory Methods: Class methods are often used as factory methods for creating instances of the class. Factory methods encapsulate the logic for creating objects and provide a centralized interface for object instantiation. This can be useful for managing object creation in complex systems or for implementing design patterns like the Factory Method pattern.
# Static Helper Methods: While class methods receive the class itself as the first parameter (cls), they are still accessible from instances of the class. This makes them useful for defining static helper methods that are related to the class but do not depend on instance state. These methods can be called both from class instances and directly from the class itself.
# Code Organization and Readability: By encapsulating related functionality within class methods, you can improve code organization and readability. Class methods provide a clear indication that the functionality is associated with the class as a whole rather than individual instances.


# class MyClass:
#     class_variables = "This is a class variables"

#     def __init__(self,value) :
#         self.instances_variable = value

#     @classmethod
#     def class_method(cls):
#         return cls.class_variables
    
# print(MyClass.class_method())


class Employee:
    company = "MIcrosoft"
    def show(self):
        print("The name is {self.name} and company is {self.company}")

    @classmethod
    def changeCompany(cls,new_company):
        cls.company = new_company

e1 = Employee()
e1.name = "Ram"
e1.show()
e1.changeCompany("Apple")
e1.show()
print(Employee.company)