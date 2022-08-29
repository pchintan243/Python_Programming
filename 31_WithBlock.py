# Using with syntax you don't remember to close the file it is automatically open and close the file

with open("chintan.txt") as f:
    a = f.readlines()
    print(a)

f = open("chintan.txt", "rt")
print(f.readlines())
print(f.readline())
f.close()
