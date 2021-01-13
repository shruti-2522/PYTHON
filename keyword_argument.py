"""def fun1(a, b, c, d):
    print(a, b, c, d)"""


# args:
def fun1(*args):
    for i in args:
        print(i)


a = ('shruti', 'niki', 'hitesh', 'pd')

fun1(*a)
