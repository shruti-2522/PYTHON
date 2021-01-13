"""simple function
a = 9
b = 10
c = sum((a, b))#Built _in function
print(c)

#USER DEFINED FUNCTION:
def fun1():
    print("Hello world")

fun1()


# function input:
def fun1(a, b):
    print("Addition:", a + b)

fun1(4, 5)"""


# function using return:
def fun2(a, b):
    """these function returns adddoition:"""
    avg = (a + b) / 3
    return avg


f = fun2(10, 20)
print(f)
