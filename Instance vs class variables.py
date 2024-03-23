
# In Python, instance variables and class variables are two types of variables used within classes, each with its own scope and behavior.

# Instance Variables:
# Instance variables are specific to each instance of a class.
# They are defined within methods of the class, typically within the __init__ method.
# Each instance of the class has its own separate copy of instance variables.
# Instance variables are accessed and modified using the instance of the class (i.e., object).
# They represent the unique state or attributes of each individual object.

# class person:
#     def __init__(self,name,age) :
#         self.name = name
#         self.age = age
# person1 = person("Ram",20)
# person2 = person("Sita",19)
# print(person1.name,person1.age)
# print(person2.name,person2.age)


# Class Variables:
# Class variables are shared among all instances of a class.
# They are defined directly within the class body but outside of any instance methods.
# Class variables are accessed using the class name.
# They represent properties or attributes that are common to all instances of the class.

# class Circle:
#     pi = 3.141

#     def __init__(self,radius) :
#         self.radius = radius

#     def area(self):
#         return self.pi*self.radius**2
    
# Circle1 = Circle(10)
# Circle2 = Circle(5)

# print(Circle1.area())
# print(Circle2.area())




