# what is function ?
- function is a block of code that performs a specific task and can be reused many times.
- instead of writing a code again and again, we define a function once and call it whenever needed.
🔹 Defining a Function
- def is the built-in keyword in Python that is used to declare functions.
Syntax
def function_name():
    code
Example:
def greet():
    print("Hello, welcome to Python!") 
- Calling the function:
greet()
Output:
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

🧠 What is Scope in Python?

Scope means:
👉 Where a variable can be accessed in your program.

— Python uses the LEGB rule to decide where to look for variables.
🧠 What is the LEGB Rule?

LEGB stands for:

L → Local

E → Enclosing

G → Global

B → Built-in

👉 Python searches for variables in this order:

Local → Enclosing → Global → Built-in
🔹 1. Local Scope (L)

Variables defined inside a function.

Example
def my_function():
    x = 10   # Local variable
    print(x)

my_function()

✅ x is only available inside the function

❌ This will cause an error:

print(x)  # Error: x is not defined

🔹 2. Enclosing Scope (E)

Variables in an outer function (used in nested functions).

Example
def outer():
    x = 20   # Enclosing variable

    def inner():
        print(x)

    inner()

outer()

👉 inner() uses x from the outer function

🔹 3. Global Scope (G)

Variables defined outside all functions.

Example
x = 50   # Global variable

def my_function():
    print(x)

my_function()

👉 Global variables can be used anywhere

🔹 Modifying Global Variable
x = 10

def change():
    global x
    x = 20

change()
print(x)

Output:
20

🔹 4. Built-in Scope (B)

These are predefined names in Python like:

print()

len()

range()

Example:

print(len("Python"))

👉 len is a built-in function

🔥 Full LEGB Example
x = "global"

def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print(x)

    inner()

outer()

Output:

local

👉 Python stops at the first match (Local)

🧠 Important Concept

If a variable is not found, Python moves:

Local → Enclosing → Global → Built-in

If still not found ❌ → Error

🧠 What is a Decorator in Python?

A decorator is a function that modifies another function without changing its code.

👉 Think of it like:

“Wrapping extra behavior around a function”

🔹 Why Use Decorators?

- Add logging
- Add authentication
- Measure execution time
- Reuse code (DRY principle)

🔹 Basic Idea (Functions are Objects)

In Python, functions can be:

- stored in variables
- passed as arguments
- returned from other functions

Example:

def greet():
    return "Hello"

say_hello = greet
print(say_hello())

🔹 Creating a Simple Decorator
Step 1: Create decorator function
def my_decorator(func):
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")
    return wrapper
Step 2: Apply decorator
@my_decorator
def say_hello():
    print("Hello!")
Step 3: Call function
say_hello()
Output:
Before function runs
Hello!
After function runs

🔥 How It Works Internally
This:

@my_decorator
def say_hello():
    print("Hello!")

is the same as:

def say_hello():
    print("Hello!")

say_hello = my_decorator(say_hello)

🔹 Decorator with Arguments
def my_decorator(func):
    def wrapper(name):
        print("Before")
        func(name)
        print("After")
    return wrapper

@my_decorator
def greet(name):
    print("Hello", name)

greet("Tsion")

🔹 Using *args and **kwargs (Important)
This makes decorator work for any function:

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result
    return wrapper

🔹 Real Example: Execution Time
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        
        result = func(*args, **kwargs)
        
        end = time.time()
        print("Time:", end - start)
        
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(2)
    print("Finished")

slow_function()

🔹 Real Example: Authentication
def login_required(func):
    def wrapper(user):
        if user != "admin":
            print("Access denied")
        else:
            func(user)
    return wrapper

@login_required
def dashboard(user):
    print("Welcome to dashboard")

dashboard("admin")

🧠 What is a Lambda Function?

A lambda function is a small anonymous (unnamed) function.

👉 Used for short, simple operations
👉 Written in one line

🔹 Syntax
lambda arguments: expression
🔹 Example 1: Simple Function

Normal function:
def add(a, b):
    return a + b

Lambda version:
add = lambda a, b: a + b

print(add(3, 5))

Output:
8

🔹 Example 2: Square
square = lambda x: x * x

print(square(4))

Output:
16
🔥 Key Rule

👉 Lambda can only have:
one expression

❌ No multiple statements
❌ No loops or assignments inside

🔹 Why Use Lambda?

Mostly used with:
- map()
- filter()
- sorted()

🔹 Example with map()
numbers = [1, 2, 3, 4]
result = list(map(lambda x: x * 2, numbers))
print(result)

Output:
[2, 4, 6, 8]

🔹 Example with filter()
numbers = [1, 2, 3, 4, 5]
result = list(filter(lambda x: x % 2 == 0, numbers))
print(result)

Output:
[2, 4]

🔹 Example with sorted()
students = [("A", 80), ("B", 60), ("C", 90)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)

Output:
[('B', 60), ('A', 80), ('C', 90)]

🔹 Lambda vs Normal Function

## Feature	      Lambda	     NormalFunction
    Name	     ❌ No name	    ✅ Has name
    Size	      Short	          Can be long
    Use	         Simple tasks	   Complex logic
    