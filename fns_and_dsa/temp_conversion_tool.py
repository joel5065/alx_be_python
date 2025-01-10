FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

input_value = input("Enter the temperature to convert: ")
if input_value.isdigit():
    temp_to_convert = input_value
else:
    print("Invalid temperature. Please enter a numeric value ")

checker = (input("Is this temperature in Celsius or Fahrenheit? (C/F)")).upper
if checker == "F":
    output_temp = convert_to_celsius(temp_to_convert)
    print(f"{temp_to_convert}°F is {output_temp}°C")
elif checker == "C":
    output_temp = convert_to_fahrenheit(temp_to_convert)
    print(f"{temp_to_convert}°C is {output_temp}°F")
else:
    print("Enter a valid input")
    