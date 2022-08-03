boolean = input("Enter the boolean expression true and false:")

a  = int(input("Enter the value:"))
if boolean == "true":
    for i in range(0, a):
        j = 0
        for j in range(j , i + 1):
            print("*",end="")
        print()
else:
    This is another way to maek it reverse
    # for i in range(a, 0, -1):
    for i in range(0, a):
        for j in reversed(range(i, a)):
            print("*",end="")
            j = j - 1
        print()