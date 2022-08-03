def fibonacci(n):
    t1, t2 = 0, 1
    i = 0
    t = t1 + t2
    # while i < n - 1:
    #     t1 = t2
    #     t2 = t
    #     t = t1 + t2
    #     i = i + 1
    # print(t1)
    if(n == 1):
        return 0
    elif(n == 2):
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Enter the value:"))
value = fibonacci(n)
print(value)
