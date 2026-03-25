## Python Exception Handling

Python Exception Handling allows a program to gracefully handle unexpected events (like invalid input or missing files) without crashing. Instead of terminating abruptly, Python lets you detect the problem, respond to it, and continue execution when possible.

- An exception is an error that occurs during program execution.
- Instead of crashing, Python lets you catch and handle it.

## Difference Between Errors and Exceptions
Errors and exceptions are both issues in a program, but they differ in severity and handling. Let's see how:

Error: Serious problems in the program logic that cannot be handled. Examples include syntax errors or memory errors.
Exception: Less severe problems that occur at runtime and can be managed using exception handling (e.g., invalid input, missing files).

🔹 Basic Syntax
try:
    # code that may cause an error
except SomeError:
    # code to handle the error

🔹 Example 1: Division by Zero
try:
    result = 10 / 0
except ZeroDivisionError:
    print("You cannot divide by zero!")

Output:
You cannot divide by zero!

🔹 Example 2: Multiple Exceptions
try:
    x = int(input("Enter a number: "))
    result = 10 / x
except ValueError:
    print("Invalid input! Enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero!")

🔹 Example 3: Catch All Exceptions
try:
    num = int(input("Enter a number: "))
    print(10 / num)
except Exception as e:
    print("An error occurred:", e)

🔹 Else and Finally
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except Exception as e:
    print("Error:", e)
else:
    print("Result is:", result)
finally:
    print("This always runs")

Explanation:
try → code that may fail
except → handle errors
else → runs if no error
finally → always runs (cleanup code)

🔹 Raising Your Own Exception
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    print("Age is", age)

check_age(-5)

Output:
ValueError: Age cannot be negative