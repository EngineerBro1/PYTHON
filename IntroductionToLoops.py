# Introduction to Loops
# Sometimes a programmer wants to execute a group of statements a certain number of times. This can be done using loops. Based on this loops are further classified into following main types;

# for loop
# while loop


#1. The for Loop:-
# for loops can iterate over a sequence of iterable objects in python. Iterating over a sequence is nothing but iterating over strings, lists, tuples, sets and dictionaries.
# example
# fruits = ["apple","banana","cherry","orange"]
# for x in fruits:
#     print(x)


# looping through a string
# for x in "banana":
#     print(x)


# using break statement in for loop( using break after print statement first printing then check untill the break statement comes)
# fruits = ["apple","banana","cherry","orange"]
# for x in fruits:
#     print(x)
#     if x =="cherry":
#         break

# using break statement but before the print function(checks break con then print)
# fruits = ["apple","banana","cherry","orange"]
# for x in fruits:
#     if x == "cherry":
#         break
#     print(x)


# using continue statement
# fruits = ["apple","banana","cherry","orange"]
# for x in fruits:
#     if x == "cherry":
#         continue
#     print(x)


# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.

# Syntax
# range(start, stop, step)
# 1.
# for x in range(6):      # printing from 0 to 6
#     print(x)
# 2.
# for x in range(2,6):   #printing from 2 to 6
#     print(x)
# 3.
# for x in range(5,50,5):     #printing from 5 to 50 with in interval of 5
#     print(x)


# ELSE IN FOR LOOP
# 4.
# for x in range(6):
#     print(x)
# else:
#     print("END")

# 5.
# for x in range(10):
#     if x == 5:
#         break
#     print(x)
# else:
#     print("Finished")


# 6. Nested Loop:- a nested loop is a inside a loop . The "inner loop " will be executed one time for each iteration of the "outer loop"
# fruits = ["apple","banana","cherry","orange"]
# property = ["red","tasty"]
# for x in property:
#     for y in fruits:
#         print(x,y)

# 7. PASS STATEMENT
#  For loop cammot be empty , but if for some reason the loop have no content , put in the pass statement to avoid getting an error.
# for x in [2.424,4,5]:
#     pass





# WHILE LOOP:-
# With the while loop we can execute a set of statements as long as a condition is true
# ayntax
# while condition:
#   statement


# a = int(input("Enter the value: "))
# i = 0
# while i<a:
#     print(i)
#     i +=1



# The break Statement
# With the break statement we can stop the loop even if the while condition is true:
# syntax
# while condition:
#   statement
#   break


# a = int(input("Enter the range value: "))
# i  = 0
# while i<a:
#     print(i)
#     if i == 10:
#         break
#     i +=1


# The continue Statement
# With the continue statement we can stop the current iteration, and continue with the next:
# syntax
# while condition:
#   statement
#       continue

# a = int(input("Enter the range value: "))
# i = 1
# while i<a:
#     i+=1
#     if i == 10:
#         continue
#     print(i)





# The else Statement
# With the else statement we can run a block of code once when the condition no longer is true:

# syntax 
# while condition:
#   statement
# else:
#   statement

# a =  int(input("Enter the range value: "))
# i = 0
# while i<a:
#     print(i)
#     i+=1
# else:
#     print("i is no longer less than a") 





# break statement
# The break statement enables a program to skip over a part of the code. A break statement terminates the very loop it lies within.

# example
for i in range(1,101,1):
    print(i ,end=" ")
    if(i==50):
        break
    else:
        print("Mississippi")
print("Thank you")


# Continue Statement
# The continue statement skips the rest of the loop statements and causes the next iteration to occur.

# example
for i in [2,3,4,6,8,0]:
    if (i%2!=0):
        continue
    print(i)



# Do-While loop in python
# do..while is a loop in which a set of instructions will execute at least once (irrespective of the condition) and then the repetition of loop's body will depend on the condition passed at the end of the while loop. It is also known as an exit-controlled loop.












































