## 1. Tuples in Python
- What is a Tuple?

A tuple is a collection of items like a list, but it is immutable.
👉 Immutable means: you cannot change the values after creating it.

Key Features:

- Ordered
- Immutable (cannot change values)
- Allows duplicate values
- Written using parentheses ( )

Example of Tuple:
fruits = ("apple", "banana", "mango")
print(fruits)

Output:
('apple', 'banana', 'mango')

- Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
- When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
- Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
- Since tuples are indexed, they can have items with the same value.
## Create Tuple With One Item
To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
e.g:
thistuple = ("apple",)
print(type(thistuple)) # prints <class 'tuple'>

#NOT a tuple
thistuple = ("apple")
print(type(thistuple)) # prints <class 'str'>

- Tuple items can be of any data type. also they can contain different data types.
e.g:  A tuple with strings, integers and boolean values:
tuple1 = ("abc", 34, True, 40, "male")
## The tuple() Constructor
It is also possible to use the tuple() constructor to make a tuple.
e.g: thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
     print(thistuple)
output: ('apple', 'banana', 'cherry')
## Range of Indexes
You can specify a range of indexes by specifying where to start and where to end the range.
When specifying a range, the return value will be a new tuple with the specified items.
e.g: Return the third, fourth, and fifth item:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
output: ('cherry', 'orange', 'kiwi')
## Change Tuple Values
Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
Example :
Convert the tuple into a list to be able to change it:

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)
output : ("apple", "kiwi", "cherry")
## Add Items
Since tuples are immutable, they do not have a built-in append() method, but there are other ways to add items to a tuple.

1. Convert into a list: Just like the workaround for changing a tuple, you can convert it into a list, add your item(s), and convert it back into a tuple.

Example
Convert the tuple into a list, add "orange", and convert it back into a tuple:

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
2. Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple:

Example
Create a new tuple with the value "orange", and add that tuple:

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)
## Remove Items
Note: You cannot remove items in a tuple.

Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround as we used for changing and adding tuple items.
Example
Convert the tuple into a list, remove "apple", and convert it back into a tuple:

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
- Or you can delete the tuple completely:

Example
The del keyword can delete the tuple completely:

thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists
## Tuple Packing

Packing means putting values into a tuple.
person = ("Tsion", 21, "Ethiopia")
## Tuple Unpacking

Extracting values from a tuple.

person = ("Tsion", 21, "Ethiopia")

name, age, country = person

print(name)
print(age)
print(country)
- Note: The number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect the remaining values as a list.
Using Asterisk*
If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:

Example
Assign the rest of the values as a list called "red":

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
- If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.

Example
Add a list of values the "tropic" variable:

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)
## Loop Through a Tuple
You can loop through the tuple items by using a for loop.
Example
Iterate through the items and print the values:

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
output: apple
        banana
        cherry
## Loop Through the Index Numbers
You can also loop through the tuple items by referring to their index number.
Use the range() and len() functions to create a suitable iterable.

Example
Print all items by referring to their index number:

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])
## Using a While Loop
You can loop through the tuple items by using a while loop.
Use the len() function to determine the length of the tuple, then start at 0 and loop your way through the tuple items by referring to their indexes.
Remember to increase the index by 1 after each iteration.
## Join Two Tuples
To join two or more tuples you can use the + operator:
Example:Join two tuples:
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3) #('a', 'b', 'c', 1, 2, 3)
## Multiply Tuples
If you want to multiply the content of a tuple a given number of times, you can use the * operator:

Example
Multiply the fruits tuple by 2:

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple) # ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')
## Tuple Methods
Python has two built-in methods that you can use on tuples.

Method	Description
count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found
