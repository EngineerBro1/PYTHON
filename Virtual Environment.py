# A virtual environment is a tool used to isolate specific Python environments on a single machine, allowing you to work on multiple projects with different dependencies and packages without conflicts. This can be especially useful when working on projects that have conflicting package versions or packages that are not compatible with each other.
# To create a virtual environment in Python, you can use the venv module that comes with Python.

# # Create a virtual environment
# python -m venv myenv

# # Activate the virtual environment (Linux/macOS)
# source myenv/bin/activate

# # Activate the virtual environment (Windows)
# myenv\Scripts\activate.bat




# Once the virtual environment is activated, any packages that you install using pip will be installed in the virtual environment, rather than in the global Python environment. This allows you to have a separate set of packages for each project, without affecting the packages installed in the global environment.

# To deactivate the virtual environment, you can use the deactivate command
# Deactivate the virtual environment
# deactivate


# The "requirements.txt" file:
# In addition to creating and activating a virtual environment, it can be useful to create a requirements.txt file that lists the packages and their versions that your project depends on. This file can be used to easily install all the required packages in a new environment.

# To create a requirements.txt file, you can use the pip freeze command, which outputs a list of installed packages and their versions.
# Output the list of installed packages and their versions to a file
# pip freeze > requirements.txt


# To install the packages listed in the requirements.txt file, you can use the pip install command with the -r flag:

# # Install the packages listed in the requirements.txt file
# pip install -r requirements.txt





# How importing in python works:
# Importing in Python is the process of loading code from a Python module into the current script. This allows you to use the functions and variables defined in the module in your current script, as well as any additional modules that the imported module may depend on.

# To import a module in Python, you use the import statement followed by the name of the module. For example, to import the math module, which contains a variety of mathematical functions, you would use the following statement:
# import math

# import math
# output = math.sqrt(16)
# print(output)

# from keyword:
# You can also import specific functions or variables from a module using the from keyword. For example, to import only the sqrt function from the math module

# from math import sqrt
# output = sqrt(16)
# print(output)

# You can also import multiple functions or variables at once by separating them with a comma

# from math import sqrt,pi
# output = sqrt(25)
# print(output)
# print(pi)


# importing everything:
# It's also possible to import all functions and variables from a module using the * wildcard. However, this is generally not recommended as it can lead to confusion and make it harder to understand where specific functions and variables are coming from.

# from math import *
# output = sqrt(25)
# print(output)

# The "as" keyword
# Python also allows you to rename imported modules using the as keyword. This can be useful if you want to use a shorter or more descriptive name for a module, or if you want to avoid naming conflicts with other modules or variables in your code.
# import math as m 
# output = m.sqrt(25)
# print(output)

# The dir function:
# Finally, Python has a built-in function called dir that you can use to view the names of all the functions and variables defined in a module. This can be helpful for exploring and understanding the contents of a new module.

import math
print(dir(math))












