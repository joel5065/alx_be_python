def perform_operation(num1, num2, operation):
    match operation:
        case "add":
            return num1 + num2
        case "subtract":
            return num1 - num2
        case "multiply":
            return num1 * num2
        case "divide":
            if num1 == 0:
                return " Provide a number different of zero"
            elif num2 == 0:
                return "Provide a number different of zero"
            else:
                return num1 / num2

    