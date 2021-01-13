""""def fun1():
    print("hello")


fun2= fun1
del fun1
"""


# You can return function through function:
# def fun1(num):
#     if num == 0:
#         return print
#     if num == 1:
#         return sum
#
# a=fun1(0)
# print(a)

def funret(fun1):
    def now():
        print("program is runninng....")
        fun1()
        print("...........")

    return now()


@funret
def msg():
    print("hello")


msg()
