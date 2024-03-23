# Length of a String
# We can find the length of a string using len() function.


# a= "Apple"
# lenth_of_a= print(len(a))
# print("Apple is a "+a+"letter length")



# String as an array
# A string is essentially a sequence of characters also called an array. Thus we can access the elements of this array.

# a= "ApplePie"
# print(a[:4])
# print(a[6])
# print(a[2:5])
# print(a[2:])
# print(a[-5:-1])


# Loop through a String:
# Strings are arrays and arrays are iterable. Thus we can loop through strings.


# a ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# for i in a:
#     print(i)


# String methods:-
# Python provides a set of built-in methods that we can use to alter and modify the strings.

# 1. upper() :
# The upper() method converts a string to upper case.


a = "AFghuehgTFh"
print(a.upper())



# 2. lower()
# The lower() method converts a string to lower case.

b="AfyhvYRUA"
print(b.lower())


# 3.strip() :
# The strip() method removes any white spaces before and after the string.


c = " Silver Moon "
print(c.strip())


# 4. rstrip() :
# the rstrip() removes any trailing characters.like special char !@#$$%%^&&

d = "Silver Moon !@#$"
print(d.rstrip("!@#$"))

# 5. replace() :
# The replace() method replaces all occurences of a string with another string.

e = "Silver Moon"
print(e.replace("Moon","Spoon"))    

# 6. split() :
# The split() method splits the given string at the specified instance and returns the separated strings as list items.


f = "Silver Moon"
print(f.split(" "))


# 7.capitalize() :
# The capitalize() method turns only the first character of the string to uppercase and the rest other characters of the string are turned to lowercase. The string has no effect if the first character is already uppercase.

g = "Silver Moon"
print(g.upper())
print(g.capitalize())




# 8. count() :
# The count() method returns the number of times the given value has occurred within the given string.

h = "Silver Moon"
print(h.count("o"))


# 9. endswith() :
# The endswith() method checks if the string ends with a given value. If yes then return True, else return False.

i = "Silver Moon"
print(i.endswith("n"))
print(i.endswith("M",4,8))



# 10. find() :
# The find() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then return -1.


j = "PYTHON IS A iNTERPRETED lANGUAGE"
print(j.lower())
print(j.find("PYTHON"))



# 11. index() :
# The index() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then raise an exception.


k = "PYTHON IS A iNTERPRETED lANGUAGE"
print(k.index("IS"))


# 12. isalnum() :
# The isalnum() method returns True only if the entire string only consists of A-Z, a-z, 0-9. If any other characters or punctuations are present, then it returns False.


l = "SilverMoon4"
print(l.isalnum())



# 13. isalpha() :
# The isalpha() method returns True only if the entire string only consists of A-Z, a-z. If any other characters or punctuations or numbers(0-9) are present, then it returns False.


m = "SilverMoon"
print(m.isalpha())



# 14. islower() :
# The islower() method returns True if all the characters in the string are lower case, else it returns False.

n = "silvermoon"
print(n.islower())


# 15. isprintable() :
# The isprintable() method returns True if all the values within the given string are printable, if not, then return False.

o = "Silver Moon"
print(o.isprintable())


# 16. isspace() :
# The isspace() method returns True only and only if the string contains white spaces, else returns False.

# p = " Silver Moon"
p ="    "
print(p.isspace())



# 17. istitle() :
# The istitile() returns True only if the first letter of each word of the string is capitalized, else it returns False.

q = "Silver Moon"
print(q.istitle())



# 18. isupper() :
# The isupper() method returns True if all the characters in the string are upper case, else it returns False.


r = " Silver Moon"
print(r.isupper())



# 19. startswith() :
# The startswith() method checks if the string starts with a given value. If yes then return True, else return False


s = "PYTHON IS A iNTERPRETED lANGUAGE"
print(s.startswith("PYTHON"))



# 20. swapcase() :
# The swapcase() method changes the character casing of the string. Upper case are converted to lower case and lower case to upper case.

t = "pYTHON IS A iNTERPRETED lANGUAGE"
print(t.swapcase())


# 21. title() :
# The title() method capitalizes each letter of the word within the string.

u = "python is a interpreted language"
print(u.title())




