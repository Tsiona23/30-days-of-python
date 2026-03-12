# write a program that asks the user for a number and print it if it's positive, neagative or zero
num = int(input("enter an number: "))
if num > 0:
    print("positive")
elif num < 0:
    print("negative")
else:
    print("zero")

# write a program that enters a number and check if it's even or odd
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
# write a program that asks a user for two numbers and print the largest one  
num1 = int(input("enter a number: ")) 
num2 = int(input("enter a number: "))
if num1 > num2:
    print("num1 is the largest")
else:
    print("num2 is the largest")    
# ask the user for marks and print the grade
score = float(input("Enter your score: "))

if score >= 90:
    print("Grade: A")
elif score >= 70:
    print("Grade: B")
elif score >= 50:
    print("Grade: C")
else:
    print("Grade: F")    