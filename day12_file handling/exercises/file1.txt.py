with open("file1.txt", "w") as file:
    file.write("Hello Python")
# Read and display content of file1.txt
with open("file1.txt", "r") as file:
    content = file.read()
    print(content)
# add this text to the file "learning  python is fun !"
with open("file1.txt", "a") as file:
    file.write("\nLearning Python is fun!")
# print each line separately
with open("file1.txt", "r") as file:
    for line in file:
        print(line.strip())

# Count how many lines are in the file
count = 0
with open("file1.txt", "r") as file:
    for line in file:
        count= count+1
print("Lines:", count)
# Count total words
with open("file1.txt", "r") as file:
    text = file.read()
    word = text.split()
    print("Words", len(word))
# Copy content from file1.txt to file2.txt
with open("file1.txt", "r") as file1:
    content = file1.read()
with open("file2.txt", "w") as file2:
    file2.write(content)
#check if the file exists before reading
import os

if os.path.exists("file1.txt"):
    print("File exists")
else:
    print("File not found")
# find the longest word in the file
with open("file1.txt", "r") as file:
    
    words = file.read().split()
    longest = max(words, key=len)
    print("The longest word:", longest)
# replace the word "Python" with "Programming"
with open("file1.txt", "r") as file:
    text = file.read()

text = text.replace("Python", "Programming")

with open("file1.txt", "w") as file:
    file.write(text)
