# This script gives you the multiplication table of a provide number


number = int(input("Enter a number to see its multiplication table: "))

for i in range(1, 11):
    print(f"{number} * {i} = ", number * i)