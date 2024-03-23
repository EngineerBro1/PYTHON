# Python allows the else keyword to be used with the for and while loops too. The else block appears after the body of the loop. The statements in the else block will be executed after all iterations are completed. The program exits the loop only after the else block is executed.


# Syntax
# for counter in sequence:
#     #Statements inside for loop block
# else:
#     #Statements inside else block

# eg

for i in range(10):
    print("iteration no{}".format(i+1))
else:
    print("else block in loop")




