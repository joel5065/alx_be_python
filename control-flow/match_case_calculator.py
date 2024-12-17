# Perform calculations using match case to select the operator

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

operator = str(input("Choose the operation (+, -, *, /): "))

match operator:
    case "+":
        print("The result is:", number1 + number2)
    case "-":
        print("The result is:", number1 - number2)
    case "*":
        print("The result is:", number1 * number2)
    case "/":
        if number2 == 0:
            print("Cannot divide by zero")   
        else:
            print("The result is:", number1 / number2)
    case _:
        print("This operator is not allowed")
