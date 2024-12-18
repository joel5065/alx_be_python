# This scripts draws a pattern 

# a variable to enter the size of the pattern

size = int(input("Enter the size of the pattern: "))

if size == 0: # Checking if the size is not zero
    print("Enter a valid size")
else:
    row = 0
    while row < size:
        for col in range(size):
            print("*", end='') # Printing the pattern
        print("") # We separe two consecutive pattern
        row += 1  # Increment the row to break the while a the end
            
        
