 🧠 What is a Module in Python?

A module is simply a file that contains Python code.

👉 It can have:

- functions
- variables
- classes

🔹 Example

Create a file called:
math_utils.py

Inside it:
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

 🔹 Using a Module
In another file:

import math_utils
print(math_utils.add(2, 3)) 

- Note: When using a function from a module, use the syntax: module_name.function_name.

## Variables in Module
The module can contain functions, as already described, but also variables of all types (arrays, dictionaries, objects etc):

- Save this code in the file mymodule.py

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}
- Import the module named mymodule, and access the person1 dictionary:

 import mymodule
a = mymodule.person1["age"]
print(a)
# Naming a Module
You can name the module file whatever you like, but it must have the file extension .py
# Re-naming a Module
You can create an alias when you import a module, by using the as keyword:
e.g :
import mymodule as mx

a = mx.person1["age"]
print(a)

🔹 Built-in Modules
Python already has many modules:
Examples:

- math
- random
- datetime
# Using the dir() Function
There is a built-in function to list all the function names (or variable names) in a module. The dir() function.
e.g:
import platform
x = dir(platform)
print(x)

- Example: math module
 import math
print(math.sqrt(16))

- Example: random module
 import random
print(random.randint(1, 10))

🔹 What is a Package?
👉 A package is a folder that contains multiple modules

Structure:
my_package/
   ├── module1.py
   ├── module2.py

   
