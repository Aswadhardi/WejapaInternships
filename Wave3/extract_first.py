# Extract First Names
# Use a list comprehension to create a new list first_names containing just the first names in names in lowercase.

names = ["Rick Sanchez", "Morty Smith",
         "Summer Smith", "Jerry Smith", "Beth Smith"]

first_names = [item.split(' ')[0].lower() for item in names]
# write your list comprehension here
print(first_names)
