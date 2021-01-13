dict1 = {'name': 'shruti', 'hobbies': 'programmimg', 1: 'Niki', 2: 'rushali'}
print(dict1)

# Add data into dictionary:
dict1[3] = "Vishakha"
dict1[4] = "Pradhunya"
print(dict1)

# del data into dictionary:
del dict1[3]
print(dict1)

# function in dictionary:
dict3 = dict1.copy()
print(dict3)
dict3 = dict1
print(dict3)

# Update:
dict1.update({3: 'hitesh'})
print(dict1)

# print keys:
print(dict1.keys())

# print items:
print(dict1.items())

# print values:
print(dict1.values())
