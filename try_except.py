# exception_handling
num1 = input("Enter number1:")
num2 = input("Enter number2")

try:
    print("addition of two nums:" + int(num1) + int(num2))
except Exception as e:
    print(e)
