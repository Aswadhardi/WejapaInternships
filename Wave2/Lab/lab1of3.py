# Use this playground to experiment with list methods, using Test Run
names = ['kwame', 'kofi', 'yaw', 'akwasi']
print(names)
print('appending aswad to the list')
names.append('aswad')
print(names)

# append()	Adds an element at the end of the list

copy_name = names.copy()
print('list of copied list ', copy_name)
# copy()	Returns a copy of the list
number_of_names = names.count('yaw')
print(f'the number of occurence of yaw in the list names is {number_of_names}')
# count()	Returns the number of elements with the specified value
new_names = ['john', 'paul', 'slyvia', 'rita']
print('the elements of new names is added to names')
print(names.extend(new_names))
print(names)
# extend()	Add the elements of a list (or any iterable), to the end of the current list
print('the index of john in the list is ')
print(names.index('john'))

# index()	Returns the index of the first element with the specified value

print('Adding hardi to the list at index 4')
names.insert(4, 'hardi')
print(names)
# insert()	Adds an element at the specified position
print('poping the 5th element out')
names.pop(5)
print(names)

# pop()	Removes the element at the specified position (5)
print('poping the last element out')
names.pop()
print(names)
# pop()	Removes the element at the last index

print(f'removing john from the list ')
names.remove('john')
print(names)
# remove()	Removes the first item with the specified value(john)

print('Reserve list of names ')
names.reverse()
print(names)
# reverse()	Reverses the order of the list
print('sorting the list')
names.sort()
print(names)
# sort()	Sorts the list
print('clearing the list')
names.clear()
print(names)
# clear()	Removes all the elements from the list
