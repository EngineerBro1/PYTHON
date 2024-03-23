# if "__name__ == "__main__" in Python:
# The if __name__ == "__main__" idiom is a common pattern used in Python scripts to determine whether the script is being run directly or being imported as a module into another script.
# In Python, the __name__ variable is a built-in variable that is automatically set to the name of the current module. When a Python script is run directly, the __name__ variable is set to the string __main__ When the script is imported as a module into another script, the __name__ variable is set to the name of the module.



# Why is it useful?:
# This idiom is useful because it allows you to reuse code from a script by importing it as a module into another script, without running the code in the original script.

# import script

# script.main()









# os Module in Python:
# The os module in Python is a built-in library that provides functions for interacting with the operating system. It allows you to perform a wide variety of tasks, such as reading and writing files, interacting with the file system, and running system commands.
 


# Reading and writing files The os module provides functions for opening, reading, and writing files. For example, to open a file for reading, you can use the open function

# import os
# Doc = os.open("file.txt.txt",os.O_RDONLY) #open file
# contents = os.read(Doc,1) #read
# os.close(Doc)


# To open a file for writing, you can use the os.O_WRONLY flag

# import os 
# Doc = os.open("file.txt.txt",os.O_WRONLY)
# os.write(Doc,b"Hello")  #write
# os.close(Doc)




# Interacting with the file system
# The os module also provides functions for interacting with the file system. For example, you can use the os.listdir function to get a list of the files in a directory

# import os
# Doc = os.listdir(".")
# print(Doc)



# You can also use the os.mkdir function to create a new directory


# import os 
# os.mkdir("newFile")



# Running system commands 
# Finally, the os module provides functions for running system commands. For example, you can use the os.system function to run a command and get the output

# import os 
# OT = os.system("cd")
# print(OT)



# You can also use the os.popen function to run a command and get the output as a file-like object

import os 
Doc = os.popen("cd")
OT = Doc.read()
print(OT)
Doc.close()






