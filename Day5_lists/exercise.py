# create a list of 5 numbers and print the first and the last one
x = [1, 2, 3, 4, 5]
print(x[0])
print(x[-1])
# add a number to the list and print the list
x.append(int(input('enter a number:')))
print(x)
# remove the second number from the list and print the list
x.pop(1)
print(x)
# reverse the list and print it
x.reverse()
print(x)
# sort the list and print it
x.sort()
print(x)
# loop through the list and print each number
for i in x:
    print(i)
# create a nested list (2*2) and access an element from it
nested_list = [[1, 2], [3, 4]]
print(nested_list[0][0])
# create list of squares from 1 to 10 using list comprehension and print it
squares =[x**2 for x in range(1, 11)]
print(squares)
# Take a list of numbers from user input (comma separated), and print the maximum and minimum number.
numbers = [int(x) for x in input('Enter numbers separated by comma: ').split(',')]
print(f'Maximum: {max(numbers)}, Minimum: {min(numbers)}')