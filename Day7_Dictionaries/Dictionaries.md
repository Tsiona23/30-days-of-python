## 🔹 What is a Dictionary?

A dictionary is a collection of key-value pairs.

Key: unique identifier (like a label)

Value: data associated with the key

Dictionaries are unordered, mutable, and indexed by keys.

Syntax
my_dict = {"key1": "value1", "key2": "value2"}

e.g 
student = {
    "name": "Tsion",
    "age": 22,
    "city": "Addis Ababa"
}

print(student) ## {'name': 'Tsion', 'age': 22, 'city': 'Addis Ababa'}

- When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.
- Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.
- Dictionaries cannot have two items with the same key
e.g 
Duplicate values will overwrite existing values:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict) # {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}
## The dict() Constructor
It is also possible to use the dict() constructor to make a dictionary.

Example
Using the dict() method to make a dictionary:

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict) #{'name': 'John', 'age': 36, 'country': 'Norway'}
- 🔹 Removing Items
e.g 
student = {
    "name": "Tsion",
    "age": 22,
    "city": "Addis Ababa"
}

student.pop("city")  # Remove by key
print(student)

student.popitem()    # Removes the last inserted item
print(student)

del student["age"]   # Delete specific key
print(student)

student.clear()      # Remove all items
print(student)       # {}

##  Loop Through a Dictionary
You can loop through a dictionary by using a for loop.

When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.
e.g
student = {"name":"Tsion","age":22,"city":"Addis Ababa"}

# Loop through keys
for key in student:
    print(key)

# Loop through values
for value in student.values():
    print(value)

# Loop through key-value pairs
for key, value in student.items():
    print(key, "->", value)
🔹 Dictionary Methods
## Method	          Description
get(key)	         Returns value of key
keys()	           Returns all keys
values()        	 Returns all values
items()          	 Returns all key-value pairs
update(dict2)	     Updates dictionary with another dict
pop(key)         	 Removes a key-value pair by key
popitem()	         Removes last inserted item
clear()	           Clears all items
copy()	           Returns a shallow copy    
## Copy a Dictionary
You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.

There are ways to make a copy, one way is to use the built-in Dictionary method copy().
## 🔹 Nested Dictionaries
e.g
students = {
    "student1": {"name":"Tsion","age":22},
    "student2": {"name":"Hiyab","age":21}
}

print(students["student1"]["name"])  # Tsion
## Loop Through Nested Dictionaries
You can loop through a dictionary by using the items() method like this:
e.g 
Example
Loop through the keys and values of all nested dictionaries:
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y]) 
output:
 child1
name: Emil
year: 2004
child2
name: Tobias
year: 2007
child3
name: Linus
year: 2011