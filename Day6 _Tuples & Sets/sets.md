## Sets in Python
What is a Set?

A set is a collection of unique items.

Key Features

- Unordered
- No duplicate values
- Mutable
- Written using curly braces { }
- * Note: Set items are unchangeable, but you can remove items and add new items. 
Example of Set:
numbers = {1, 2, 3, 4}
print(numbers)
- Duplicate Values are Removed
e.g
numbers = {1, 2, 2, 3, 4, 4}
print(numbers)
Output:{1, 2, 3, 4}
- Unordered means that the items in a set do not have a defined order.
Set items can appear in a different order every time you use them, and cannot be referred to by index or key.
- Set items are unchangeable, meaning that we cannot change the items after the set has been created.
Once a set is created, you cannot change its items, but you can remove items and add new items.
- Set items can be of any data type:

Example
String, int and boolean data types:

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
- A set can contain different data types:

Example
A set with strings, integers and boolean values:

set1 = {"abc", 34, True, 40, "male"}
## The set() Constructor
It is also possible to use the set() constructor to make a set.

Example
Using the set() constructor to make a set:
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
- You cannot access items in a set by referring to an index or a key.
But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.

Example
Loop through the set, and print the values:

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
  - Once a set is created, you cannot change its items, but you can add new items.

- To add one item to a set use the add() method.

Example
Add an item to a set, using the add() method:
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset) # {'apple', 'orange', 'cherry', 'banana'}
- To add items from another set into the current set, use the update() method.

Example
Add elements from tropical into thisset:

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset) # {'apple', 'mango', 'cherry', 'pineapple', 'banana', 'papaya'}
- The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
- To remove an item in a set, use the remove(), or the discard() method.
Note: If the item to remove does not exist, remove() will raise an error.
Note: If the item to remove does not exist, discard() will NOT raise an error.
- You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.
The return value of the pop() method is the removed item.
Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.
## Adding Elements to a Set
numbers = {1, 2, 3}
numbers.add(4)
print(numbers) # {1, 2, 3, 4}
## Removing Elements
numbers = {1, 2, 3}
numbers.remove(2)
print(numbers)
Output:{1, 3}
## Set Operations
- Union
Combines two sets.

A = {1, 2, 3}
B = {3, 4, 5}

print(A | B)
Output: {1,2,3,4,5}

- Intersection
Common elements.

A = {1, 2, 3}
B = {2, 3, 4}

print(A & B)
Output:{2,3}

- Difference
Elements in A but not in B.

A = {1,2,3}
B = {2,3,4}

print(A - B)
Output: {1}
## Python frozenset
frozenset is an immutable version of a set.
Like sets, it contains unique, unordered, unchangeable elements.
Unlike sets, elements cannot be added or removed from a frozenset.
## Creating a frozenset
Use the frozenset() constructor to create a frozenset from any iterable.
Example
Create a frozenset and check its type:

x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x)) # frozenset({'cherry', 'banana', 'apple'})
<class 'frozenset'>

## Frozenset Methods
Being immutable means you cannot add or remove elements. However, frozensets support all non-mutating operations of sets.

## Method	       Shortcut	     Description	
copy()	 	                      Returns a shallow copy	
difference()	      -	             Returns a new frozenset with the difference	
intersection()	      &	             Returns a new frozenset with the intersection	
isdisjoint()	 	             Returns whether two frozensets have an intersection	
issubset()	        <= / <	        Returns True if this frozenset is a (proper) subset of another	
issuperset()         >= / >	        Returns True if this frozenset is a (proper) superset of another	
symmetric_difference()	^   	Returns a new frozenset with the symmetric differences	
union()               	|	                    Returns a new frozenset containing the union	
## Set Methods
Python has a set of built-in methods that you can use on sets.

## Method	            Shortcut	           Description
add()	 	                         Adds an element to the set
clear()	 	                          Removes all the elements from the set
copy()	 	                         Returns a copy of the set
difference()	             -	          Returns a set containing the difference between two or more sets
difference_update()         -=	   Removes the items in this set that are also included in another, specified set
discard()	 	                   Remove the specified item
intersection()	             &	     Returns a set, that is the intersection of two other sets
intersection_update()        &=	   Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	 	                Returns whether two sets have a intersection or not
issubset()	                  <=	  Returns True if all items of this set is present in another set
 	                          <	    Returns True if all items of this set is present in another, larger set
issuperset()	               >=	  Returns True if all items of another set is present in this set
 	                           >	 Returns True if all items of another, smaller set is present in this set
pop()	                    	    Removes an element from the set
remove()	 	                     Removes the specified element
symmetric_difference()       	^	        Returns a set with the symmetric differences of two sets
symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another
union()	                        |	Return a set containing the union of sets
update()	                   |=	Update the set with the union of this set and others


