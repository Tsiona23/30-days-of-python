# what is function ?
- function is a block of code that performs a specific task and can be reused many times.
- instead of writing a code again and again, we define a function once and call it whenever needed.
🔹 Defining a Function
Syntax
def function_name():
    code
Example:
def greet():
    print("Hello, welcome to Python!") 
- Calling the function:
greet()

Output
Hello, welcome to Python!
## Function Names
Function names follow the same rules as variable names in Python:

- A function name must start with a letter or underscore
- A function name can only contain letters, numbers, and underscores
- Function names are case-sensitive (myFunction and myfunction are different)

🔹 Function with Parameters
A parameter allows us to pass information to a function.

Example:
def greet(name):
    print("Hello", name)

Call the function:

greet("Tsion")

Output:
Hello Tsion

🔹 Function with Multiple Parameters
def add(a, b):
    result = a + b
    print("Sum =", result)

add(5, 3)

Output:
Sum = 8

🔹 Function with Return Value
Instead of printing the result, a function can return a value.

def add(a, b):
    return a + b

result = add(4, 6)

print("Sum =", result)

Output:
Sum = 10
