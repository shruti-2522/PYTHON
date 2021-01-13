# itterative function:
def factorial_itterative(n):
    fact = 1
    for i in range(n):
        fact = fact * (i + 1)
    return fact


def factorial_recursive(n):
    if n == 1:
        return n
    else:
        return n * factorial_recursive(n - 1)


n = int(input("ENTER ANY NUMMBER:"))
print("Factorail is calculated by itterative manner", factorial_itterative(n))
print("Factorial is calculated by Recursive manner", factorial_recursive(n))
