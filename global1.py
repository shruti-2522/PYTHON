l = 10  # Global
def add(a, b):
    # l = 5 #local
    m = 10  # local
    global l
    l = l + 70
    print("addition", l + m)


add(5, 10)
print(l)
