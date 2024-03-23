# Python Modules
# Consider a module to be the same as a code library.
# A file containing a set of functions you want to include in your application

# Create a Module:
# To create a module just save the code you want in a file with the file extension .py


# Use a Module:
# Now we can use the module we just created, by using the import statement
# import mymodule
# mymodule.greeting("Ram")

# Variables in Module
# The module can contain functions, as already described, but also variables of all types (arrays, dictionaries, objects etc)
# import mymodule
# print(mymodule.person["name"])

# Naming a Module:
# You can name the module file whatever you like, but it must have the file extension .py


# Re-naming a Module:
# You can create an alias when you import a module, by using the as keyword
# import mymodule as mm
# print(mm.person["name"])

# Built-in Modules:
# There are several built-in modules in Python, which you can import whenever you like.
# import platform
# print(platform.system())

# Using the dir() Function:
# There is a built-in function to list all the function names (or variable names) in a module. The dir() function
# import platform
# print(dir(platform))

# Import From Module:
# You can choose to import only parts from a module, by using the from keyword.

# from mymodule import person
# print(person["age"])






# Python Datetime:

# Python Dates:
# A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.
# import datetime
# time = datetime.datetime.now()
# print(time.year)
# print(time.strftime("%A"))


# Creating Date Objects:
# To create a date, we can use the datetime() class (constructor) of the datetime module.
# The datetime() class requires three parameters to create a date: year, month, day.

# import datetime
# date = datetime.datetime(2024,2,19)
# print(date)


# The strftime() Method:
# The datetime object has a method for formatting date objects into readable strings.
# The method is called strftime(), and takes one parameter, format, to specify the format of the returned string

# import datetime
# date = datetime.datetime(2024,2,19)
# print(date.strftime("%A"))


# A reference of all the legal format codes:

# Directive	Description	                                                     Example	
# %a	        Weekday, short version	                                         Wed	
# %A	        Weekday, full version	                                         Wednesday	
# %w	        Weekday as a number 0-6, 0 is Sunday	                         3	
# %d	        Day of month 01-31	                                             31	
# %b	        Month name, short version	                                    Dec	
# %B	        Month name, full version	                                    December	
# %m	        Month as a number 01-12	                                        12	
# %y	        Year, short version, without century	                        18	
# %Y	        Year, full version	                                            2018	
# %H	        Hour 00-23	                                                    17	
# %I	        Hour 00-12	                                                    05	
# %p	        AM/PM	                                                        PM	
# %M	        Minute 00-59	                                                41	
# %S	        Second 00-59	                                                08	
# %f	        Microsecond 000000-999999	                                    548513	
# %z	        UTC offset	                                                    +0100	
# %Z	        Timezone	                                                    CST	
# %j	        Day number of year 001-366	                                    365	
# %U	        Week number of year, Sunday as the first day of week, 00-53	    52	
# %W	        Week number of year, Monday as the first day of week, 00-53	    52	
# %c	        Local version of date and time	                                Mon Dec 31 17:41:00 2018	
# %C	        Century	                                                        20	
# %x	        Local version of date	                                        12/31/18	
# %X	        Local version of time	                                        17:41:00	
# %%	        A % character	                                                %	
# %G	        ISO 8601 year	                                                2018	
# %u	        ISO 8601 weekday (1-7)	                                        1	
# %V	        ISO 8601 weeknumber (01-53)	                                    01


































