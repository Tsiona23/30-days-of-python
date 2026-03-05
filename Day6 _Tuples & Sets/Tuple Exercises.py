# create a tuple and print it
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
# create a tuple with different data types and print it 
my_tuple2 = ("Tsion", 21, 1.70, True)
print(my_tuple2)
# create a tuple with one element and print it
my_tuple3 = (42,)
print(my_tuple3)
# unpack a tuple and print the values
name, age, height, is_student = my_tuple2
print(name)
print(age)
print(height)
print(is_student)
# create a tuple of tuples
my_tuple4 = ((1, 2), (3, 4), (5, 6))
print(my_tuple4)
# create a tuple from list andprint it
my_list = [7, 8, 9]
my_tuple5 = tuple(my_list)
print(my_tuple5)
# create a tuple of 5 numbers and print the length of the tuple
my_tuple3 = (1, 2, 3, 4, 5)
print(len(my_tuple3))
# create a tuple of 5 numbers from keyboard input and print the sum of the numbers
numbers = []
for i in range(5):
    num = int(input("Enter a number:"))
    numbers.append(num)
    my_tuple6 = tuple(numbers)
print(my_tuple6)
# write a program if an item is found in the tuple or not
my_tuple7 = (10, 20, 30, 40, 50)
item = int(input("enter an item to check"))
if item in my_tuple7:
    print("Item found in the tuple")
else:
    print("Item not found in the tuple")
# write a program that converts a tuple in to a list and add an item to the list and convert back to a tuple and print it
my_tuple8 = (1, 2, 3)   
my_list = list(my_tuple8)
my_list.append(4)
my_tuple8 = tuple(my_list)
print(my_tuple8)
# print all the elements in the tuple using a for loop
my_tuple9 = ("apple", "banana", "cherry")
for x in my_tuple9:
    print(x)
# write a program that counts how many times an item appears in a tuple
mt_tuple10 = (1, 2, 3, 4, 5, 1, 2, 1)
item = int(input("Enter an item to count: "))
count = mt_tuple10.count(item)
print(f"The item {item} appears {count} times in the tuple.")
# write a program that finds the index of an item in atuple
my_tuple11 = ("a", "b", "c", "d", "e")
item = input("Enter an item to find its index: ")
try:
    index = my_tuple11.index(item)
    print(f"The item {item} is at index {index}.")
except ValueError:
    print(f"The item {item} is not in the tuple.")
