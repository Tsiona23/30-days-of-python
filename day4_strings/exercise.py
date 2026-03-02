# write a program that takes a name as input and prints the name i uppercase, lowercase, and title case
name = input("Enter your name: ")
print(name.upper())
print(name.lower())
print(name.title()) 
# write a program that takes a sentence as input and counts how many characters it has
x = input("Enter a sentence:")
print(len(x))
# print the word in reverse order
y = "English"
print(y[::-1])
# write a program that takes a full name as input and prints the first and last character, total length, and name without spaces
full_name = input("enter your full name:")
print("First character:", full_name[0])
print("Last character:", full_name[-1])
print("Total length:", len(full_name))
print("Name without spaces:", full_name.replace(" ", ""))
# write a program that takes a string as input and checks if it is a palindrome(a word that reads the same backwords)
palindrome = input("Enter a word to check if it is a palindrome: ")
if palindrome == palindrome[::-1]:
    print("The word is a palindrome.")
else:
    print("The word is not a palindrome.")
# write a program that takes a string as input and counts how many times a specific character appears in the string
string = input('enter a string:')
character = input('enter a character to count:')
count = string.count(character)
print(f"The character '{character}' appears {count} times in the string.")
