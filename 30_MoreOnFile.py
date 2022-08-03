f = open("chintan.txt")

# tell() function is use to find where is your file pointer
print(f.readline())
print(f.tell())

# seek() function is find to use return your file pointer at that position
f.seek(33)
print(f.readline())
# print(f.tell())
f.close()
