list1 = ["11", "22", "33", "44"]
"""for i in range(len(list1)):
    print(list1[i])
a = int(list1[2]) + 1;
print(a)"""
a = list(map(int, list1))
a[2] = a[2] + 1;


# print((a[2]))

# Map function using simple fun:
def sq(num):
    return num * num


num = [1, 2, 3, 4, 5, 67, 8]
# b=list(map(sq,num))
# print(b)

# using lambda function:
c = list(map(lambda x: x * x, num))
print(c)
