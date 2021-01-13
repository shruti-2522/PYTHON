s = set()
print(type(s))

s = set([1, 2, 3, 4, 5])
print(s)

# add data:
s.add(6)
print(s)

# remove
s.remove(3)
print(s)

# union:
s1 = s.union([23, 34, 56])
print(s1)

# Intersection:
s2 = s.intersection([1, 2])
print(s2)


