# ask the user for two numbers and devide them 
# Handle: ZeroDivisionError, and ValueError
try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Result:", a / b)
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid input!")

# Convert String to Integer Handle:If user enters text → show "Invalid number!"

try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("Invalid number!")