# Browse the complete list of string methods at:
# https://docs.python.org/3/library/stdtypes.html#string-methods
# and try them out here. Endeavor to copy the link without the first # comment sign beginning it.

welcome = ' Hello world!!'
print(welcome)
print(welcome.upper())
# returns copy of the string converted to uppercased
print(welcome.lower())
# returns copy of the string converted to lowercased
print(welcome.islower())
# returns true if the string is lower cased
print(welcome.isupper())
# returns true if the string is uppper cased
print(welcome.isalpha())
print('hello123'.isalpha())
# returns true if the string is alphabetic
print('hello123'.isalnum())
# returns true if the string is alphanumeric
print('123'.isdecimal())
# returns true if the string is a decimal
print('    '.isspace())
# returns true if the string is a space
print('This Is Title Case'.istitle())
print('This Is Title Case 123'.istitle())
print('This Is not Title Case'.istitle())
# returns true if the string is title_cased
print(welcome.startswith('Hello'))
# returns true if the string startswith the argument
print(welcome.endswith('world!'))
# returns true if the string endswith the argument
print(welcome.split())
# splits the string into a list of words
print(welcome.rjust(10))
print(welcome.rjust(20))
# right justifies the string with length width 20
print(welcome.center(20))
# centers the string with 20 length width
print(welcome.strip())
# removes all whitespaces leading and trailing
