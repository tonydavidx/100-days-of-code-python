import random
# numbers = [1, 2, 3]

# new_numbers = [n+1 for n in numbers]


# name = 'Tony'

# new_list = [letter for letter in name]

# range_list = [n*2 for n in range(1, 5)]


# names = ['Tony', 'Lisa', 'Michael', 'Ginger', 'Jackson', 'Nicole']

# names_upper = [n.upper() for n in names if len(n) > 5]


# dictionary comprehencion

names = ['Tony', 'Lisa', 'Michael', 'Ginger', 'Jackson', 'Nicole']

student_scores = {student: random.randint(1, 100) for student in names}
passed_students = {student: score for(
    student, score) in student_scores.items() if score > 50}

print(student_scores)
print(passed_students)
