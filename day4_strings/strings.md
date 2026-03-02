## What is a String?

A string is a sequence of characters (text).
Strings in python are surrounded by either single quotation marks, or double quotation marks.
'hello' is the same as "hello".
- You can use quotes inside a string, as long as they don't match the quotes surrounding the string.
e.g   
print("It's alright")
print("she is called 'Tsion'")
print('she is called "Tsion"')
output: It's alright
       she is called 'Tsion'
       she is called "Tsion"
- you can also use Triple quotes """ """ (for multi-line)
## Assign String to a Variable
Assigning a string to a variable is done with the variable name followed by an equal sign and the string.
e.g   a = "Hello"
       print(a)       
output: Hello
## Strings are Arrays
Like many other popular programming languages, strings in Python are arrays of unicode characters.
However, Python does not have a character data type, a single character is simply a string with a length of 1.
Square brackets can be used to access elements of the string.
e.g
a = "Hello, World!"
print(a[1])
output: e
## String Length
To get the length of a string, use the len() function.
e.g
word = "Python"
print(len(word))
output: 6
##  Check String
- To check if a certain phrase or character is present in a string, we can use the keyword in.
- To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
e.g 
txt = "The best things in life are free!"
print("free" in txt)
print("also" not in txt)
output: True
        True
## String Slicing
You can return a range of characters by using the slice syntax.
Specify the start index and the end index, separated by a colon, to return a part of the string.
Syntax:
string[start:end]
e.g 
word = "Python"
print(word[0:4])
Output: Pyth
It means: from index 0 to 3 (4 not included).
- Slice From the Start
By leaving out the start index, the range will start at the first character.
e.g  b = "Hello, World!"
     print(b[:5])
output: Hello
- Slice To the End
By leaving out the end index, the range will go to the end.
e.g
b = "Hello, World!"
print(b[2:])
output: llo, World
## Negative Indexing
Use negative indexes to start the slice from the end of the string.
-> Important Notes
- Negative indices start from -1, not -0 (which would be the same as 0)
- Using an index beyond the sequence length raises an IndexError
- Works with any sequence type: strings, lists, tuples, etc.
 Negative indexing is particularly useful when you need to access elements from the end without knowing the exact length of the sequence.
 e.g 
 text = "Python"
# Index:  0  1  2  3  4  5
#         P  y  t  h  o  n
#        -6 -5 -4 -3 -2 -1

print(text[-1])  # 'n' (last character)
print(text[-2])  # 'o' (second last)
print(text[-3])  # 'h'
print(text[-4])  # 't'
print(text[-5])  # 'y'
print(text[-6])  # 'P'

# With Lists
fruits = ['apple', 'banana', 'orange', 'grape']
print(fruits[-1])   # 'grape'
print(fruits[-2])   # 'orange'
print(fruits[-3])   # 'banana'
print(fruits[-4])   # 'apple'
# With Slicing Using Negative Indices
text = "Python Programming"

- Get last 3 characters
print(text[-3:])     # 'ing'
- Get all except last 5 characters
print(text[:-5])     # 'Python Progr'
- Get characters from index 2 to second last
print(text[2:-2])    # 'thon Programmi'
- Reverse a string
print(text[::-1])    # 'gnimmargorP nohtyP'
## Python - Modify Strings
Python has a set of built-in methods that you can use on strings.

- Upper Case
The upper() method returns the string in upper case.
e.g
a = "Hello, World!"
print(a.upper())
output: HELLO, WORLD!
- Lower Case
The lower() method returns the string in lower case.
e.g
a = "Hello, World!"
print(a.lower())
output: hello, world!
- Remove Whitespace
Whitespace is the space before and/or after the actual text, and very often you want to remove this space.
The strip() method removes any whitespace from the beginning or the end.
e.g 
a = " Hello, World! "
print(a.strip())
output: Hello, World!
- Replace String
The replace() method replaces a string with another string.
e.g   a = "Hello, World!"
      print(a.replace("H", "J"))
output: Jello, World!
- Split String
The split() method returns a list where the text between the specified separator becomes the list items.
e.g a = "Hello, World!"
    b = a.split(",")
     print(b)
output: ['Hello', ' World!']
## String Concatenation(joining strings)
To concatenate, or combine, two strings you can use the + operator.
e.g a = "Hello"
    b = "World"
    print(a + " " + b)
output: Hello World    
## Escape Character
To insert characters that are illegal in a string, use an escape character.
An escape character is a backslash \ followed by the character you want to insert.
An example of an illegal character is a double quote inside a string that is surrounded by double quotes.
e.g 
txt = "my name is \"Tsion\" and i am a student."
print(txt) 
output: my name is "Tsion" and i am a student.
- Why Do We Need Escape Characters?
Because sometimes we want to:
Print quotes inside a string
Move to a new line
Add a tab space
Print a backslash
🔹 Common Escape Characters
| Escape | Meaning         |
| ------ | --------------- |
| `\'`   | Single quote    |
| `\"`   | Double quote    |
| `\\`   | Backslash       |
| `\n`   | New line        |
| `\t`   | Tab space       |
| `\b`   | Backspace       |
| `\r`   | Carriage return |

## String Methods
Python has a set of built-in methods that you can use on strings.
Note: All string methods return new values. They do not change the original string.

## Method	                   Description
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isascii()	Returns True if all characters in the string are ascii characters
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning

