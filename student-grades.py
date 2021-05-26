student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}

# Scores 91 - 100: Grade = "Outstanding"
# Scores 81 - 90: Grade = "Exceeds Expectations"
# Scores 71 - 80: Grade = "Acceptable"
# Scores 70 or lower: Grade = "Fail"

# Adds the grades to student_grades

for student in student_scores:

    if student_scores[student] > 90:
        student_grades[student] = "Outstanding"

    elif student_scores[student] > 80:
        student_grades[student] = "Exceeds Expectations"

    elif student_scores[student] > 70:
        student_grades[student] = "Acceptable"

    else:
        student_grades[student] = "Fail"


print(student_grades)
