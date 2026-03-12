## What is an If Statement?

An if statement lets a program execute code only if a condition is true.

Basic Syntax
if condition:
    code_to_run

Example:
age = 18
if age >= 18:
    print("You are an adult")

Output:
You are an adult

## 🔹 If – Else Statement

If the condition is false, the else block runs.
e.g:
age = 16
if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")

Output:
You cannot vote

## 🔹 If – Elif – Else

Use elif when you have multiple conditions.
e.g:
score = 75

if score >= 90:
    print("Grade A")
elif score >= 70:
    print("Grade B")
elif score >= 50:
    print("Grade C")
else:
    print("Fail")

Output:
Grade B

## 🔹 Comparison Operators (used in if)
##  Operator	 Meaning
    ==	         equal
    !=        	not equal
    >	        than
    <	       less than
    >=	       greater or equal
    <=	       less or equal

Example:
x = 10
if x == 10:
    print("x is ten")

## 🔹 Logical Operators
Operator	Meaning
and	both conditions must be true
or	one condition must be true
not	reverses condition

Example:
age = 20
citizen = True
if age >= 18 and citizen:
    print("You can vote")    