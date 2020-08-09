# Count By Check
# Suppose you want to count from some number start_num by another number count_by until you hit a final number end_num, and calculate break_num the way you did in the last quiz.

# Now in addition, address what would happen if someone gives a start_num that is greater than end_num. If this is the case, set result to "Oops! Looks like your start value is greater than the end value. Please try again." Otherwise, set result to the value of break_num.


start_num = 5  # provide some start number
end_num = 15  # provide some end number that you stop when you hit
count_by = 2  # provide some number to count by

# write a condition to check that end_num is larger than start_num before looping
# write a while loop that uses break_num as the ongoing number to
#   check against end_num
break_num = count_by
while start_num < end_num:
    break_num += 1
    if break_num == end_num+1:
        count_by += end_num
        break
else:
    print('Oops! Looks like your start value is greater than the end value. Please try again.')
    break_num = count_by
print(break_num)

print(result)
