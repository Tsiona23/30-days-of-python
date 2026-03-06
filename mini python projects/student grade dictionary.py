# create a program that stores student names and grades in a dictionary, prints all students,finds the highest geade,calculates the average grade

# Store student names and grades in a dictionary
grades = {
    "Abel": 75,
    "Hana": 90,
    "Tsion": 85,
    "Meron": 80
}

# Print all students
print("All students:")
for student in grades:
    print(student)

print("\n" + "-" * 30)  # Separator line

# Find the highest grade
highest_student = max(grades, key=grades.get)
highest_grade = grades[highest_student]

print(f"Highest grade: {highest_student} with {highest_grade}")

print("-" * 30)  # Separator line

# Calculate the average grade
total_grades = sum(grades.values())
num_students = len(grades)
average_grade = total_grades / num_students

print(f"Total marks: {total_grades}")
print(f"Number of students: {num_students}")
print(f"Average grade: {average_grade:.2f}")