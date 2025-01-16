def safe_divide(numerator : float, denominator: float):
    try:
        result  = float(numerator) / float(denominator)
        print(f"The result of the division is {result:.1f}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except TypeError:
        print("Error: Please enter numeric values only.")