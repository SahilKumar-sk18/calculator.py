a = int(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ")
b = int(input("Enter second number: "))

if op == "+":
    print("The sum of two numbers is:", a + b)  

elif op == "-":
    print("The difference of two numbers is:", a - b)

elif op == "*":
    print("The product of two numbers is:", a * b)

elif op == "/":
    print("The quotient of two numbers is:", a / b)
else:
    print("Invalid operator. Please use +, -, *, or /.")