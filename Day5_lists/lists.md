## 🔹 What is a List?

A list is a collection of items in a particular order.
- Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
- Lists are mutable → you can change items after creating them.
- Lists are created using square brackets:
e.g 
thislist = ["apple", "banana", "cherry"]
print(thislist) 
- Lists can contain different types (numbers, strings, booleans, even other lists).
e.g 
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4]
mixed = [1, "apple", True, 5.5]
## 🔹 Accessing List Items

Use indexing (starts at 0).
fruits = ["apple", "banana", "cherry"]

print(fruits[0])   # apple
print(fruits[2])   # cherry
- Negative indexing counts from the end.
print(fruits[-1])  # cherry
print(fruits[-2])  # banana
🔹 Slicing Lists
numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])   # [20, 30, 40]
print(numbers[:3])    # [10, 20, 30]
print(numbers[2:])    # [30, 40, 50]
print(numbers[::2])   # [10, 30, 50]
🔹 Changing List Items
Lists are mutable → you can modify items.
To change the value of a specific item, refer to the index number.
e.g 
fruits = ["apple", "banana", "cherry"]
fruits[1] = "orange"
print(fruits)  # ['apple', 'orange', 'cherry']
🔹 List Methods (Most Used)
## Method	            Description
 append(x)	        Add x at the end
 insert(i, x)	  Add x at index i
 extend(list2)	  Add all items from another list
 remove(x)	     Remove first occurrence of x
 pop()	         Remove last item (or at index)
 clear()	     Remove all items
 sort()	        Sort ascending
 reverse()	    Reverse list order
 index(x)	    Find index of x
 count(x)    	Count occurrences of x
 copy()	       Create a copy of the list
 e.g :
 fruits = ["apple", "banana", "cherry"]

fruits.append("orange") # To add an item to the end of the list, use the append() method.
print(fruits)  # ['apple', 'banana', 'cherry', 'orange']

fruits.insert(1, "kiwi") # To insert a list item at a specified index, use the insert() method.
print(fruits)  # ['apple', 'kiwi', 'banana', 'cherry', 'orange']

fruits.remove("banana") # The remove() method removes the specified item.
print(fruits)  # ['apple', 'kiwi', 'cherry', 'orange']

fruits.pop() # The remove() method removes the specified item.
print(fruits)  # ['apple', 'kiwi', 'cherry']

fruits.reverse() #
print(fruits)  # ['cherry', 'kiwi', 'apple']

🔹 Checking List Items
fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)    # True
print("orange" not in fruits) # True
🔹 List Length
fruits = ["apple", "banana", "cherry"]
print(len(fruits))   # 3
🔹 Nested Lists (List Inside List)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0][1])  # 2
🔹 Looping Through a List
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

🔹 List Comprehension (Advanced but Very Useful)
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(squares)  # [1, 4, 9, 16, 25]

## N.B   List items are ordered, changeable, and allow duplicate values.
- When we say that lists are ordered, it means that the items have a defined order, and that order will not change.If you add new items to a list, the new items will be placed at the end of the list.
- The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.
- Since lists are indexed, lists can have items with the same value.
e.g  
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist) # ['apple', 'banana', 'cherry', 'apple', 'cherry']
