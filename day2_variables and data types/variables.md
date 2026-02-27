##        variables and data types 
  
  Variables and data types are the basic building blocks of Python programs.

##         1. what is variable in python ?
     A variable is a name used to store a value in memory.
Think of a variable like a container that holds data.
-python has no command for declaring a variable.
-A variable is created the moment you first assign a value to it.
    e.g  name = "Tsion"
         height = 1.7
     Here:
     name stores a string.
     height stores a decimal number.
Variables do not need to be declared with any particular type, and can even change type after they have been set.
   e.g  x = 4        # x is of type int
        x = "Sally"  # x is now of type str
        print(x)
        output : sally
    if you want to specify the data type of the variable it can be done with CASTING.
    e.g    x = str(3)    # x will be '3'
           y = int(3)    # y will be 3
           z = float(3)  # z will be 3.0
           output:      3
                        3
                        3.0
##     variable names
  variable names are case sensitive.
Rules for Python variable names:
    -A variable name must start with a letter or the underscore character.
    -A variable name cannot start with a number.
    -A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ ).
    -A variable name cannot be any of the Python keywords.
##        Variable Assignment
  -Single Assignment      e.g     x = 10
  -Multiple Assignment    e.g     a, b, c = 1, 2, 3   
  -Same Value Assignment  e.g     x = y = z = 5
##       Checking Variable Type 
  Use type() function: 
  e.g     x = 10
          print(type(x))
output : <class 'int'>
