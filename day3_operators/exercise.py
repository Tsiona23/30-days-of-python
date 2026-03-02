# write a program that takes two numbers and prints the Addition, Subtraction, Multiplication, Division, Modulus 
x = 5
y = 10
print("addition:", x+y)
print("subtraction:", x-y)
print("multiplication:", x*y)
print("division:", x/y)
print("modulus:", x%y)

# write a program if a number is even or odd using modulus operator
num = 7
if num%2 == 0:
    print(num, "is even")
else:
    print(num, "is odd")
# write a program to check if the number is positive, negative or zero
x = -3
if  x > 0 :
    print(x, "is positive")
elif x < 0:
    print(x, "is negative")
else:
    print(x, "is zero")
# write a program to check if the number is divisible by 5 and 11
num = 10
if num%5 ==0 and num%11 == 0:
    print(num, "is divisible by 5 and 11")
else: print (num, "is not divisible by 5 and 11")
# write a program to check the number is a leap year or not
year = 2026
if (year%4 == 0 and year%100 !=0) or (year%400 ==0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")
# write a program that takes a number and prints the multiplication table of that number
num = 5
for i in range(1, 11):
    print(num, "x", i, "=", num*i)
# write a program that checks if age is grater than 18 and prints"adult" otherwise prints "minor"
age = 20
if age>18:
    print("adult")
else: print("minor")