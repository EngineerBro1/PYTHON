#  conditional statements
# Sometimes the programmer needs to check the evaluation of certain expression(s), whether the expression(s) evaluate to True or False. If the expression evaluates to False, then the program execution follows a different path than it would have if the expression had evaluated to True.
# Based on this, the conditional statements are further classified into following types:

# if
# if-else
# if-else-elif
# nested if-else-elif.


#1. if statement:--
# if the expression evaluates True:
# Execute the block of code inside if statement. After execution return to the code out of the if……block
# SYNTAX
# if condition:
    # statement
# 


# age = int (input("Enter your age : "))
# if age>=18: 
#     print("You are eligible to vote")





# 2.  if……else statement:--
# if the expression evaluates True:
# Execute the block of code inside if statement. After execution return to the code out of the if……else block.\

# if the expression evaluates False:
# Execute the block of code inside else statement. After execution return to the code out of the if……else block.

# SYNTAX
# if condition:
#   statement1
# else:
#   statement2


# x = int (input("Entere first num: "))
# y = int(input("Enter the second num: "))
# if x<y: print("x is less than y")
# else: print("x is greater than y ")

# OR YOU CAN WRITE IN ALSO 

# if x<y: 
#     print("x is less than y")
# else: 
#     print("x is greater than y ")




# 3.if-else-elif:-
# Sometimes, the programmer may want to evaluate more than one condition, this can be done using an elif statement.
# Working of an elif statement
# Execute the block of code inside if statement if the initial expression evaluates to True. After execution return to the code out of the if block.
# Execute the block of code inside the first elif statement if the expression inside it evaluates True. After execution return to the code out of the if block.
# Execute the block of code inside the second elif statement if the expression inside it evaluates True. After execution return to the code out of the if block.
# Execute the block of code inside the nth elif statement if the expression inside it evaluates True. After execution return to the code out of the if block.
# Execute the block of code inside else statement if none of the expression evaluates to True. After execution return to the code out of the if block.

# SYNTAX
# if condition1:
#   statement1
# elif condition2:
#   statement2
# .
# .
# .
# else:
#   statement n

# x = int(input("Enter the First num: "))
# y = int(input("Enter the second num: "))
# if x>y:
#     print("x is greater than y")
# elif x<y:
#     print("x is less than y")
# else:
#     print("x is equal to y")


# 4.Nested if statements
# Nested if-else statement in python allow you to test multiple conditions and execute different code blocks based on the result of test 
# syntax
#if condition1: 
#   execute condition1 true
#   if condition2:
#       execute both the condition1 and condition2 are true
#   else:
#       execute if conditon1 is true but condition2 is false
# else:
#   execute if condition1 is false


# num = 21
# if num>0:
#     if num%2 ==0:
#         print("The number is positive and even")
#     else:
#         print("The number is positive but odd")
# else:
#     print("The number is negative")

# 
# NESSTED IF-ELSE WITH ELIF
# a password and username checking


# username = input("Enter your username: ")
# password = input("Enter your password: ")
# if username == "python":
#     if password == "9452":
#         print("Login Succcessful! WElcome")
#     elif password == "1234":
#         print("Weak password. Please reset your password")
#     else:
#         print("Incorrect password. Please try again after sometime")
# else:
#     if username == "guest":
#         if password == "guest":
#             print("Login successful! welcome Guest")
#         else:
#             print("Incorrect password. Please try again after sometime")
#     else:
#         print("Unknown User! Please try again")        




# Match Case Statements:--
# A match statement will compare a given variable’s value to different shapes, also referred to as the pattern. The main idea is to keep on comparing the variable with all the present patterns until it fits into one.
# The match case consists of three main entities :
# The match keyword
# One or more case clauses
# Expression for each case
# The case clause consists of a pattern to be matched to the variable, a condition to be evaluated if the pattern matches, and a set of statements to be executed if the pattern matches.
# SYNTAX
# match variable_name:
#             case ‘pattern1’ : //statement1
#             case ‘pattern2’ : //statement2
#             …            
#             case ‘pattern n’ : //statement n


command = input("Enter the command: ")
match command:
    case 'Hello':
        print("Hello to you too!")
    case 'Goodbye':
        print("See you later")
    case other:
        print("No match")


























































