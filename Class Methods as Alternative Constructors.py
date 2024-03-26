# Using class methods as alternative constructors is a common pattern in Python. It allows you to define multiple ways to create instances of a class with different initialization parameters or formats. This is particularly useful when you want to provide flexibility in how objects are created without cluttering the class with multiple __init__() methods.

# class Person:
#     def __init__(self,name,age) :
#         self.name = name
#         self.age = age

#     @classmethod
#     def  from_birth_year(cls, name, birth_year):
#         current_year = 2024 
#         age = current_year - birth_year
#         return cls(name,age)
    
# Person1 = Person("Ram",30)
# print(Person1.name,Person1.age)

# Person2 = Person.from_birth_year("Ram",1994)
# print(Person2.name,Person2.age)


class Employee:
    def __init__(self,name , salary) :
        self.name = name
        self.salary = salary

    @classmethod
    def fromStr(cls,string):
        return cls(string.split(" ")[0], int(string.split(" ")[1]))
    
emp1 = Employee("Hari",100000)
print(emp1.name)
print(emp1.salary)

string = "John-Doe 50000"
emp2 = Employee.fromStr(string)
print(emp2.name)
print(emp2.salary)

