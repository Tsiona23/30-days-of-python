# create a function that prints hello python learner!
def greet():
    print("Hello, Python Learner!")

greet()

# create a function that takes a name prints 
def greet(name):
    print("Hello", name)

greet("tsion")

#create a functin that returns the sum of two numbers
def add(a, b):
    return a + b

result = add(5, 3)
print(result)

#check if a number is even or odd
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(check_even_odd(7))

#Return the largest of three numbers
def find_max(a, b, c):
    return max(a, b, c)

print(find_max(3, 7, 5))

#count vowles
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    
    for char in text:
        if char in vowels:
            count += 1
    
    return count

print(count_vowels("Python"))