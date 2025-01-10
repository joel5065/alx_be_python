FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius
    
def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

temp_to_convert = float(input("Enter the temperature to convert: "))

if temp_to_convert.is_integer:
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
    if unit == "F":
        output_temp = convert_to_celsius(temp_to_convert)
        print(f"{temp_to_convert}°F is {output_temp}°C")
    elif unit == "C":
        output_temp = convert_to_fahrenheit(temp_to_convert)
        print(f"{temp_to_convert:.1f}°C is {output_temp:.1f}°F")
    else:
        print("Enter a valid input")
else:
     raise ValueError("Invalid temperature. Please enter a numeric value ")

    