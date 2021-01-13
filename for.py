"""prrint element of list:
l = [1, 2, 3, 5, 6, 7]
for i in l:
    print(i)"""

# print element of list of list:
nsk_frnds = [["Hitesh", 1], ["Niki", 2], ["Rushali", 3], ["Pradhunya", 4], ["Vishkha", 5]]
dict1 = dict(nsk_frnds)
print(dict1)
# for i, j in nsk_frnds:
for i, j in dict1.items():
    print(i, "Rank", j)
