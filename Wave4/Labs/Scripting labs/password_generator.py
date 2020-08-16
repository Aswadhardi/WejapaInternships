import random
# Write a function called generate_password that selects three random words from the list of words word_list and concatenates them into a single string. Your function should not accept any arguments and should reference the global variable word_list to build the password.

# Use an import statement at the top

word_file = "c:/Users/ASWAD/Desktop/New folder (2)/Wave4/Labs/Scripting labs/words.txt"
word_list = []

# fill up the word_list
with open(word_file, 'r') as words:
    for line in words:
        # remove white space and make everything lowercase
        word = line.strip().lower()
        # don't include words that are too long or too short
        if 3 < len(word) < 8:
            word_list.append(word)

# Add your function generate_password here
# It should return a string consisting of three random words
# concatenated together without spaces


def generate_password():
    generated_password = "".join(random.choices(word_list, k=3))
    return generated_password


# test your function
print(generate_password())
