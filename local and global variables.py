# local and global variables:

# Variable:
# A variable is a named location in memory that stores a value. In Python, we can assign values to variables using the assignment operator =


# a = 4 #integer
# b = "Hello"  #String
# # etc

# local variable:
# A local variable is a variable that is defined within a function and is only accessible within that function. It is created when the function is called and is destroyed when the function returns.


# global variable
# a global variable is a variable that is defined outside of a function and is accessible from within any function in your code.

# a = 4 #global variable
# def myfunction():
#     b = 67  #local variable
#     print(b)
# myfunction()
# print(a)
# print(b) #error because b is local variable only called within the function defined 




# a = 4 #global variable
# def myfunction():
#     global a
#     a = 2  # now the global variable is updated to 2
#     b = 67  #local variable
#     print(b)
# myfunction()
# print(a)
# # print(b) #error because b is local variable only called within the function defined 









# File Handling:
# Before we can perform any operations on a file, we must first open it. Python provides the open() function to open a file. It takes two arguments: the name of the file and the mode in which the file should be opened. The mode can be 'r' for reading, 'w' for writing, or 'a' for appending.

# doc = open("file.txt")  #only open file
# doc = open("file.txt",'r')


# Modes in file:
# There are various modes in which we can open files.
# read (r): This mode opens the file for reading only and gives an error if the file does not exist. This is the default mode if no mode is passed as a parameter.
# write (w): This mode opens the file for writing only and creates a new file if the file does not exist.
# append (a): This mode opens the file for appending only and creates a new file if the file does not exist.
# create (x): This mode creates a file and gives an error if the file already exists.
# text (t): Apart from these modes we also need to specify how the file must be handled. t mode is used to handle text files. t refers to the text mode. There is no difference between r and rt or w and wt since text mode is the default. The default mode is 'r' (open for reading text, synonym of 'rt' ).
# binary (b): used to handle binary files (images, pdfs, etc).




# Reading from a File:
# Once we have a file object, we can use various methods to read from the file.
# The read() method reads the entire contents of the file and returns it as a string.

# a = open('file.txt','r')
# c = a.read()
# print(c)
# print(a.read(3))

# Read Lines:
# You can return one line by using the readline() method
# a = open('file.txt','r')
# print(a.readline())


# Close Files:
# It is a good practice to always close the file when you are done with it.
# a = open('file.txt','r')
# print(a.readline())
# a.close()

# Writing to a File:
# To write to a file, we first need to open it in write mode.
# We can then use the write() method to write to the file.

# a = print(open('file.txt','w'))
# print(a)
# a = open('file.txt','w')
# print(a.write('hye'))


# a  = open('file.txt','a')
# a.write('Hello')


# Closing a File:
# It is important to close a file after you are done with it. This releases the resources used by the file and allows other programs to access it.
# To close a file, you can use the close() method.

# a = open('file.txt','r')
# a.close()



# The 'with' statement:
# Alternatively, you can use the with statement to automatically close the file after you are done with it.

# with open('file.txt','r') as a:

# Delete a File:
# To delete a file, you must import the OS module, and run its os.remove() function

# import os
# os.remove("file.txt")




# Check if File exist:
# To avoid getting an error, you might want to check if the file exists before you try to delete it

import os 
if os.path.exists("file.txt"):
    os.remove("file.txtx")
else:
    print("File doesnot exist")


# Delete Folder
# To delete an entire folder, use the os.rmdir() method


