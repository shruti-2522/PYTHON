# filter_function
"""num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 14, 45, 67]


def is_gretter_5(num):
    return num > 5


val = list(filter(is_gretter_5, num))
print(val)"""

# REDUCE FUNCTION

from functools import reduce

num1 = [20, 30, 40, 59]
a = reduce(lambda x, y: x + y, num1)
print(a)
