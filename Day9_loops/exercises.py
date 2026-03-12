#  write a program that prints numbers from 1-10
for i in range(1, 11):
    print(i)

# print even numbers from 1 to 20
for i in range(1, 21):
    if i % 2 == 0:
        print(i)

# write a program that prints sum of numbers from 1-10
sum = 0
for i in range(1, 11):
     sum = sum + i
     print( "sum =", sum)     
# write a program that asks the user to enter a word and count how many characters it has using a loop.
word = input("Enter a word: ")
count = 0
for char in word:
    count += 1
print("Number of characters:", count)