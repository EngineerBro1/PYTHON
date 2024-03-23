#  Python Constructor:
# In Python, a constructor is a special method within a class that is automatically called when a new instance of the class is created. It is typically named __init__()

# Types of Constructors in Python:
# Parameterized Constructor
# Default Constructor

# Parameterized Constructor in Python:
# When the constructor accepts arguments along with self, it is known as parameterized constructor.
# These arguments can be used inside the class to assign the values to the data members.

# class Details:
#     def __init__(self,animal,group):
#         self.animal = animal
#         self.group = group

# object = Details("Crab","Crustaceans")
# print(object.animal,"Belongs to the",object.group,"group.")



# Default Constructor in Python:
# When the constructor doesn't accept any arguments from the object and has only one argument, self, in the constructor, it is known as a Default constructor.

  
# class Details:
#     def __init__(self):
#         print("Animal Crab belongs to Crustaceans group")
# object = Details()
        


# class Myclass:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b

# object = Myclass("2","6")
# print(object.a)
# print(object.b)

        























