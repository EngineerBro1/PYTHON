# Python String Formatting
# To make sure a string will display as expected, we can format the result with the format() method.
# String format()
# The format() method allows you to format selected parts of a string.
# Sometimes there are parts of a text that you do not control, maybe they come from a database, or user input?
# To control such values, add placeholders (curly brackets {}) in the text, and run the values through the format() method
# example
# price = 50
# product = "The price is {} Rupees"
# print(product.format(price))



# Multiple Values
# If you want to use more values, just add more values to the format() method
# price = 100
# quantity = 10
# product_name = "chocolate"
# order = "I want {} pieces of product name {} for {} rupees "
# print(order.format(quantity,product_name,price))




# Index Numbers
# You can use index numbers (a number inside the curly brackets {0}) to be sure the values are placed in the correct placeholders

# price = 100  # index "0"
# quantity = 10 # index "1"
# product_name = "chocolate" # index "2"
# order = "I want {0} pieces of product name {1} for {2} rupees "
# print(order.format(quantity,product_name,price))



# Named Indexes
# You can also use named indexes by entering a name inside the curly brackets {carname}, but then you must use names when you pass the parameter values txt.format(carname = "Ford")

# car = "I have a {carname}, it is a {model}"
# print(car.format(carname = "Ford",model = "Mustang"))
# print(car.format(carname = "Porsche",model = "911"))
















































