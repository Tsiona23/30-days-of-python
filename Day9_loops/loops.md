## loops in python
 Loops are essential for automating repetitive tasks and controlling the flow of a program. 
 Python has two primary types of loops: the for loop (for iterating over sequences) and the while loop (for repeating based on a condition).
 ## for Loops
A for loop is used for iterating over a sequence (such as a list, tuple, dictionary, set, or string). This is useful when you know the number of iterations in advance or want to process each item in a collection. 
Syntax:
for item in sequence:
#code block to execute for each item

- # Example iterating over a list:
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit) # apple
                   banana
                   cherry
 # Example Loop Through a String
for letter in "Python":
    print(letter)
Output:
P
y
t
h
o
n       

- # Using range():
 The range() function generates a sequence of numbers and is often used with for loops to repeat an action a specific number of times.
 e.g:
 for i in range(5):
    print(i) # Prints 0 through 4

# while Loops
A while loop repeatedly executes a block of code as long as a specified condition remains True. This is ideal when the number of iterations is not known beforehand and depends on a dynamic condition.
Syntax:
while condition_is_true:
    # code block to execute
    # remember to update the condition variable to avoid an infinite loop
Example:
count = 0
while count < 5:
    print(count)
    count += 1 # Increments the counter to eventually make the condition False

🔹 Break Statement:
Stops the loop immediately
e.g :
for i in range(10):
    if i == 5:
        break
    print(i)
output: 0
        1
        2
        3
        4
🔹 Continue Statement
Skips the current iteration.
e.g :
for i in range(5):
    if i == 2:
        continue
    print(i)
output: 0
        1
        3
        4
        
