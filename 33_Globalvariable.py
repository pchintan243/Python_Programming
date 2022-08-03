# Global variable cannot be modified
l = 10 #global variable
def function1(n):
    m = 5 #local variable

    # for change the global value
    global l
    l = l + 10
    print(l)
    print(n, "I have printed")


function1("This is me")
print(l)

def func():
    x = 20
    def hello():
        global x
        x = 80
    print("Before calling hello()", x)
    hello()
    print("After calling hello()", x)

func()
print(x)