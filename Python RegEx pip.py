# # Python RegEx:
# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
# RegEx can be used to check if a string contains the specified search pattern.
# RegEx Module:
# Python has a built-in package called re, which can be used to work with Regular Expressions.

# import re
# dat = "Share, Learn, Connect & Explore Career options"
# a = re.search("^Share.*options$",dat)
# if a:
#     print("yes,we have match")
# else:
#     print("No match")

# RegEx Functions   
# The re module offers a set of functions that allows us to search a string for a match:

# Function	    Description
# findall	    Returns a list containing all matches
# search	    Returns a Match object if there is a match anywhere in the string
# split	        Returns a list where the string has been split at each match
# sub	        Replaces one or many matches with a string


# Metacharacters
# Metacharacters are characters with a special meaning:

# Character	    Description	                                     Example	
# []	        A set of characters	                            "[a-m]"	
# \	            Signals a special sequence      	            "\d"	
# .	            Any character                   	            "he..o"	
# ^	            Starts with	                                    "^hello"	
# $	            Ends with	                                    "planet$"	
# *	            Zero or more occurrences	                    "he.*o"	
# +	            One or more occurrences         	            "he.+o"	
# ?	            Zero or one occurrences	                        "he.?o"	
# {}	        Exactly the specified number of occurrences	    "he.{2}o"	
# |	            Either or	                                    "falls|stays"	
# ()	        Capture and group	 	 




# The findall() Function:
# The findall() function returns a list containing all matches.

# import re
# dat = "Share, Learn, Connect & Explore Career options"
# a = re.findall("re",dat)
# print(a)


# The search() Function:
# The search() function searches the string for a match, and returns a Match object if there is a match.
# If there is more than one match, only the first occurrence of the match will be returned
# If no matches are found, the value None is returned

# import re
# dat = "Share, Learn, Connect & Explore Career options"
# a = re.search("\s",dat)
# print("The first white-space character is located in position: ", a.start())

# The split() Function:
# The split() function returns a list where the string has been split at each match

# import re
# dat = "Share, Learn, Connect & Explore Career options"
# a = re.split("\s",dat)
# print(a)

# The sub() Function:
# The sub() function replaces the matches with the text of your choice

# import re
# dat = "Share, Learn, Connect & Explore Career options"
# a = re.sub("\s","5",dat)
# print(8)

# Match Object:
# A Match Object is an object containing information about the search and the result.
# The Match object has properties and methods used to retrieve information about the search, and the result:
# .span() returns a tuple containing the start-, and end positions of the match.
# .string returns the string passed into the function
# .group() returns the part of the string where there was a match


import re
dat = "Share, Learn, Connect & Explore Career options" 
a = re.search(r"\bC\w+",dat) #Search upper case C character in the bigining of a word, and print its position
print(a.span())
print(a.string)
print(a.group())




# Python PIP:

# What is PIP?:
# PIP is a package manager for Python packages, or modules if you like.

# What is a Package?
# A package contains all the files you need for a module.

# Modules are Python code libraries you can include in your project.



















