# Program Features : Ask user for student name. Ask for 3 subject scores, Calculate average and Print grade
name = input("enter student name:")

subject1 = float(input("enter score for subject 1: "))
subject2 = float(input("enter score for subject 2: "))
subject3 = float(input("enter score for subject 3: "))

average = (subject1 + subject2 + subject3) / 3
grade = ""

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
else:
    grade = "C"

print(f"Student Name: {name}")
print(f"Average Score: {average}")
print(f"Grade: {grade}")