def sq(a):
    return a * a;


def cube(a):
    return a * a * a


func = [sq, cube]
for i in range(5):
    val = list(map(lambda x: x(i), func))
    print(val)
