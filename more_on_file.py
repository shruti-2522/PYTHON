f = open("shruti.txt")
f.tell()
# f.tell()-function used for find position of file pointer:
# print(f.tell())
# seek()-function  used for reset file ptr:
print(f.seek(2))
print(f.readline())
# print(f.tell())
print(f.readline())
# print(f.tell())
print(f.readline())
f.close()
