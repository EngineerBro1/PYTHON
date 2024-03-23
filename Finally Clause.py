# Finally Clause:
# The finally code block is also a part of exception handling. When we handle exception using the try and except block, we can include a finally block at the end. The finally block is always executed, so it is generally used for doing the concluding tasks like closing file resources or closing database connection or may be ending the program execution with a delightful message.



# Syntax:
# try:
#    #statements which could generate 
#    #exception
# except:
#    #solution of generated exception
# finally:
#     #block of code which is going to 
#     #execute in any situation


# eg
try:
    num = int(input("Enter a string: "))
except ValueError:
    print("It is not a string.")
else:
    print("String accepted.")
finally:
    print("This block always executed.")


# ------------------------------------------------------------

try:
    l = [5,2,1]
    i = int(input("Enter the index: "))
    print(l[i])
    
except:
    print("some error.")

finally:
    print("Always executed")





# Raising Custom errors
# In python, we can raise custom errors by using the raise keyword


money = int(input("Enter the ammount: "))
if not 10000<money<500000:
    raise ValueError("Not valid")






# Defining Custom Exceptions:
# In Python, we can define custom exceptions by creating a new class that is derived from the built-in Exception class.


# syntax
# class CustomError(Exception):
#   # code ...
#   pass
# try:
#   # code ...
# except CustomError:
#   # code...











