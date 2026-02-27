##       Data Types in Python

A data type tells Python what kind of value a variable stores.
Main Python data types:

# Numeric Types
1. Integer (int)
Whole numbers.
e.g   x = 10
      y = -5
      print(type(x))
output: <class 'int'>
 2. Float (float)
Decimal numbers.
e.g    price = 10.5
       height = 1.75
output: <class 'float'>
3. Complex (complex)
Numbers with imaginary part.   
e.g  z = 2 + 3j
output: <class 'complex'>

# Text Type
1. String (str)
Used for text.
e.g    name = "Tsion"
       message = "Hello"
       print(type(name))
output: <class 'str'>
strings can use both double or single quote like:
     "Hello"
     'Hello'  
# Boolean Type
Boolean stores True or False. 
e.g
is_student = True
passed = False
output: <class 'bool'>
# Sequence Types
1. List
A list stores multiple values.
e.g 
numbers = [1, 2, 3, 4]
Lists use square brackets []
2. Tuple
Similar to list but cannot be changed.
e.g
coordinates = (10, 20)
Tuples use parentheses ()
3. Range
Stores a sequence of numbers.
e.g
x = range(5)
output: 0 1 2 3 4
# Set Type
Stores unique values.
e.g
colors = {"red", "blue", "green"}
Sets use curly brackets {}
Duplicates are removed automatically.
e.g 
x = {1,1,2,2,3}
print(x)
output: {1,2,3}
# Dictionary Type
Stores data in key-value pairs.
student = {
    "name": "Tsion",
    "hight": 1.70
}
output: {'name': 'Tsion', 'hight': 1.70}
