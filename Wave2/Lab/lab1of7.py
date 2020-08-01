verse_dict = {'if': 3, 'you': 6, 'can': 3, 'keep': 1, 'your': 1, 'head': 1, 'when': 2, 'all': 2, 'about': 2, 'are': 1, 'losing': 1, 'theirs': 1, 'and': 3, 'blaming': 1, 'it': 1, 'on': 1, 'trust': 1, 'yourself': 1, 'men': 1, 'doubt': 1, 'but': 1, 'make': 1, 'allowance': 1, 'for': 1, 'their': 1,
              'doubting': 1, 'too': 3, 'wait': 1, 'not': 1, 'be': 1, 'tired': 1, 'by': 1, 'waiting': 1, 'or': 2, 'being': 2, 'lied': 1, 'don\'t': 3, 'deal': 1, 'in': 1, 'lies': 1, 'hated': 1, 'give': 1, 'way': 1, 'to': 1, 'hating': 1, 'yet': 1, 'look': 1, 'good': 1, 'nor': 1, 'talk': 1, 'wise': 1}
print(verse_dict, '\n')

# number of unique keys in the dictionary
num_keys = len(verse_dict.keys())
print(num_keys)

# 'breathe' is a key in the dictionary
contains_breathe = 'breathe' in verse_dict.keys()
print(contains_breathe)

# a list of the dictionary's  sorted keys
sorted_keys = sorted(verse_dict.keys())

# getting the first element in the sorted list of keys
print(sorted_keys[0])

# printing the element with the highest value in the list of keys
print(max(list(verse_dict.keys())))
# the first key in verse dict
bonus_question_what_is_the_first_key_in_verse_dict = list(verse_dict.keys())[
    0]
print(bonus_question_what_is_the_first_key_in_verse_dict)
