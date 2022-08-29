"""
"r" - Open file for reading
"w" - Open file for writing
"x" - Creates file for if not exists
"a" - Add more content to a file
"t" - Text mode
"b" - Binary mode
"+" - Read and write
"""

f = open("chintan.txt", "rt")  # read text mode by default
# content = f.read()
# print(content)
# f.close()

# content = f.read(4)  # It reads first 4 character
# print(content)
# f.close()

# Print one line using readline function
# print(f.readline())
# print(f.readline())
# print(f.readline())

# If you want to read line by line
# for line in f:
#     print(line, end="")

# File print as a list using readlines function
# print(f.readlines())
