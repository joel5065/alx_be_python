# Perform calculations using match case to select the operator

 # Get user input for numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))      

# Get user input for operation
operation = input("Choose the operation (+, -, *, /): ").strip()

      # Perform calculation using match case
match operation:
    case "+":
        result = num1 + num2
        print(f"The result is: {result}")
    case "-":
        result = num1 - num2
        print(f"The result is: {result}")
    case "*":
        result = num1 * num2
        print(f"The result is: {result}")
    case "/":
        if num2 == 0:
            print("Error: Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"The result is: {result}")
    case _:
          print("Invalid operation. Please choose +, -, *, or /.")