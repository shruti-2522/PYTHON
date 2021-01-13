str1 = "I just do programming"
# len() function return length of string:
print(len(str1))

# print(str1[0:10:2])
print(str1[::-1])  # rev string

print(str1[-7:-2])

# upper-case:
# print(str1.upper())

# Lower-case:
print(str1.lower())

# Check string is alphanumeric:
print(str1.isalnum())
print(str1.isalpha())

# Captalize:
print(str1.capitalize())

# replace
print(str1.replace("do", "love"))

# find_position:
print(str1.find('i'))

# count:
print(str1.count())
