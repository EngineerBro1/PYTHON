# The Walrus Operator, formally known as the assignment expression operator (:=), was introduced in Python 3.8. It allows you to assign a value to a variable as part of an expression.
# The syntax is straightforward: variable := expression. The value of the expression is assigned to the variable, and the value of the expression is also the result of the entire assignment expression.


#without Walrus Operator
# name = input("Enter your Name: ")
# if len(name)>0:
#     print(f"Hello,{name}")
# else:
#     print("Name is Empty")

# #with Walrus Operator
# if(name := input("Enter your Name: ")) !="":
#     print(f"Hello,{name}")
# else:
#     print("Name is empty")



#without Walrus Operator
while True:
    user_input = input("Enter 'Quit' to Exit: ")
    if user_input == "Quit":
        break

#with Walrus Operator
while (user_input := input("Enter 'Quit' to Exit: ")) !="Quit":
    pass
