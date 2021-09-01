student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.

student_grades = {}
# TODO-2: Write your code below to add the grades to student_grades.👇
for student in student_scores:
    print(student)
    marks = student_scores[student]
    if marks > 90:
        student_grades[student] = "Outstanding"
    elif marks > 80:
        student_grades[student] = "Exceeds Expectations"
    elif marks > 70:
        student_grades[student] = 'Acceptable'
    else:
        student_grades[student] = 'Fail'

# 🚨 Don't change the code below 👇
print(student_grades)
