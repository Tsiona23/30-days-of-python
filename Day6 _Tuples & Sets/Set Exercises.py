# create a set and print it
my_set = {1, 2, 3, 4, 5}
print(my_set)
# create a set with different data types and print it
my_set2 = {"Tsion", 21, 1.70, True}
print(my_set2)
# create a set from a list and print it
my_list = [1, 2, 3, 4, 5]
my_set3 = set(my_list)
print(my_set3)
# add an item to a set and print it
my_set4 = {1, 2, 3}
my_set4.add(4)
print(my_set4)
# remove an item from a set and print it
my_set5 = {1, 2, 3,  4, 5}
my_set5.remove(4)
print(my_set5)
#  check if an item is in a set and print the result
my_set6 = {1, 2, 3, 4, 5}
item = int(input("enter an item to check:"))
if item in my_set6:
    print("item found:")
else:
    print("item not found")
# write a program that finds the union of two sets and prints them
set1 ={1, 2, 3}
set2 ={3, 4, 5}
union_set = set1.union(set2)
print(union_set)
# write a program that finds the intersection of two sets and prints it
set3 = {"a", "b", "c"}
set4 = {"b", "c", "d"}
intersection_set = set3.intersection(set4)
print(intersection_set)
# write a program that finds the difference between two sets and prints it
set5 = {"a", "b", "c"}
set6 = {1, 2, "a", "b"}
difference_set = set5.difference(set6)
print(difference_set)
# write a program that finds the symmetric difference between two sets and prints it
set7 ={1, 2, 3, 4}
set8 = {3, 4, 5, 6}
symmetric_difference_set = set7.symmetric_difference(set8)
print(symmetric_difference_set)
