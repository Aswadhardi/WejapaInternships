# Factorials with For Loops
# Now use a for loop to find the factorial!

# It will now be great practice for you to try to revise the code you wrote above to find the factorial of a number, but this time, using a for loop. Try it in the code editor below!

# number to find the factorial of
number = 6

# start with our product equal to one
product = 1

# write your for loop here
for num in range(1, number):
    product += product*num


# print the factorial of number
print(product)
