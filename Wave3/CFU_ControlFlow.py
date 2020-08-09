# Question: What type of loop should we use?
# While loop
# You need to write a loop that takes the numbers in a given list named num_list:
#num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]

# Your code should add up the odd numbers in the list, but only up to the first 5 odd numbers together. If there are more than 5 odd numbers, you should stop at the fifth. If there are fewer than 5 odd numbers, add all of the odd numbers.

# Would you use a while or a for loop to write this code?


# Please use this space to test and run your code

num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542,
            87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]
odd_numbers_sum = 0
n = 0
odd_count = 0
while odd_count < 5:
    if num_list[n] % 2 == 1:
        odd_numbers_sum += num_list[n]
        odd_count += 1
    n += 1

print(odd_numbers_sum)
