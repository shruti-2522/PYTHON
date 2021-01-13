n1 = int(input("Enter Rows:"))
n2 = int(input("type 1 or 0"))
new = bool(n2)
if new == True:
    for i in range(1, n1 + 1):
        for j in range(1, i + 1):
            print("*", end=" ")
        print()
elif new == False:
    for i in range(n2, 0, -1):
        for j in range(1, i + 1):
            print("*", end=" ")
        print()
