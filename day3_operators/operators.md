##   Operators in Python 🐍

Operators are symbols used to perform operations on variables and values.

## Types of Operators in Python

Python has 7 main types of operators:

-Arithmetic Operators
-Assignment Operators
-Comparison Operators
-Logical Operators
-Identity Operators
-Membership Operators
-Bitwise Operators

1. Arithmetic Operators ➕➖✖➗

Used for mathematical calculations.

##   Operator	 Meaning      Example	  Result
        +	     Addition	       5 + 3	 8
        -	     Subtraction	   5 - 3	 2
        *	     Multiplication    5 * 3	 15
        /	     Division	       5 / 2	 2.5
       //	     Floor Division	   5 // 2	 2
       %	     Modulus	       5 % 2	 1
      **	      Power            2 ** 3	 8

2. Assignment Operators 📥

Used to assign values to variables.

## Operator	   Example	       Meaning
    =	       x = 5	       Assign value
    +=         x += 3	       x = x + 3
    -=	       x -= 3	       x = x - 3
    *=	       x *= 3	       x = x * 3
    /=	       x /= 3	       x = x / 3
    //=	       x //= 3	       x = x // 3
    %=	       x %= 3	       x = x % 3

## 3. Comparison Operators ⚖️

Used to compare two values.

Result is True or False.

## Operator	   Meaning	     Example
      ==	    Equal	      5 == 5
      !=	   Not equal 	  5 != 3
      >	      Greater than	  5 > 3
      <       Less than	      5 < 3
     >=	   Greater or equal	  5 >= 5
     <=	   Less or equal	  5 <= 3

##  4. Logical Operators 🧠

Used to combine conditions.

## Operator	     Meaning  	     Example
     and	    Both True	     x>5 and y<10
     or	        One True	     x>5 or y<3
     not	    Reverse result	 not(x>5)

##  5. Identity Operators 🆔
Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location.

## Operator	                   Description         	                              Example
    is             Returns True if both variables are the same object              x is y
   is not	       Returns True if both variables are not the same object          x is not y

## 6. Membership Operators 📦
Membership operators are used to test if a sequence is presented in an object.

## Operator	         Description	           Example
     in              exists                     x in y
     not in          does not exist             x not in y

##  7. Bitwise Operators (Advanced) ⚙️
Bitwise operators are used to compare (binary) numbers.

## Operator    	Name            Description	                                      Example	
     &       	AND	       Sets each bit to 1 if both bits are 1	               x & y	
     |	        OR	       Sets each bit to 1 if one of two bits is 1	           x | y	
     ^	        XOR	       Sets each bit to 1 if only one of two bits is 1	       x ^ y	
     ~	        NOT	       Inverts all the bits	                                     ~x	
    <<       left shift	   Shift left by pushing zeros in from the right and let the leftmost bits  
                        falloff                                                  	x << 2	        
    >>      right shift	   Shift right by pushing copies of the leftmost bit in from the left, and let the   
              rightmost bits fall off	                                            x >> 2