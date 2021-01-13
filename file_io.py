# open:
f = open("shruti.txt", "r")  # read mode is by default
content = f.read()
print(f.readlines())
"""for i in content:
    print(content, end="")"""

f.close()
