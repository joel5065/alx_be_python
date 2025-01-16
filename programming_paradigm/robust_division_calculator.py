def safe_divide(numerator : float, denominator: float):
    try:
        result  = float(numerator) / float(denominator)
        return f"The result of the division is {result:.1f}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except:
        return "Error: Please enter numeric values only."