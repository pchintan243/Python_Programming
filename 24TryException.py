num1 = input("Enter the number1:")
num2 = input("Enter the number2:")
try:
    print("The sum of two number is:", int(num1) + int(num2))

except Exception as e:
    print(e)
    print("This is very important to execute.")
