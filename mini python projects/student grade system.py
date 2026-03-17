#Create a system that:Takes student marks,Calculates average, and Assigns grade.
def calculate_average(marks):
    return sum(marks) / len(marks)


def assign_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "F"


def student_result(marks):
    avg = calculate_average(marks)
    grade = assign_grade(avg)
    
    print("Average:", avg)
    print("Grade:", grade)


# Example usage
marks = [80, 70, 90]
student_result(marks)