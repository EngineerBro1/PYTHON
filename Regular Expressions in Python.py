# Regular expressions, often abbreviated as regex or regexp, are a powerful tool for pattern matching and text manipulation in Python. The re module in Python provides support for working with regular expressions.

# Basic Pattern Matching::

# import re
# pattern = r"hello"
# pattern = r"Hello"

# text = "Hello World"
# match = re.search(pattern,text)

# if match:
#     print("Pattern Found")
# else:
#     print("Pattern not found")


# Using Special Characters::
# Regular expressions support various special characters and sequences for more complex pattern matching:
# .: Matches any character except newline.
# ^: Matches the start of the string.
# $: Matches the end of the string.
# *: Matches zero or more occurrences of the preceding character.
# +: Matches one or more occurrences of the preceding character.
# ?: Matches zero or one occurrence of the preceding character.
# \: Escapes special characters.

# import re
# pattern = r"^hello.*world$"
# text = "hello Python world"
# if re.match(pattern, text):
#     print("Pattern found")
# else:
#     print("Pattern not found")


# Using Character Classes::
# Character classes allow you to match specific sets of characters:
# [abc]: Matches any character a, b, or c.
# [a-z]: Matches any lowercase letter.
# [0-9]: Matches any digit.
# [^abc]: Matches any character except a, b, or c.

# import re
# pattern = r"[0-9]+"
# text = "The Number is 50"
# matches = re.findall(pattern,text)
# print(matches)



# import re
# pattern = r"(\w+)(\w+)"
# text = "Keshave"
# match = re.match(pattern,text)
# if match:
#     print("Name : ", match.group())

# import re
# pattern = r"\bcat\b"
# text = "The cat and the fish"
# replacement = "dog"
# new_text = re.sub(pattern,replacement,text)
# print(new_text)