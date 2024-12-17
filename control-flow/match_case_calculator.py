# Perform calculations using match case to select the operator

number1 = int(input("Enter the first number"))
number2 = int(input("Enter the second number:"))

operator = str(input("Choose the operation (+, -, *, /):")).lower

match operator:
    case operator if operator == "+":
        print("The result is:", number1 + number2)
    case operator if operator == "-":
        print("The result is:", number1 - number2)
    case operator if operator == "*":
        print("The result is:", number1 * number2)
    case operator if operator == "/":
        print("The result is:", number1 / number2)
    case _:
        print("This operator is not allowed")
