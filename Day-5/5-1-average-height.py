students_heights = input('Input a list of Student heights: ').split()

for n in range(0, len(students_heights)):
    students_heights[n] = int(students_heights[n])

print(students_heights)

students = 0
for i in students_heights:
    i = i + i
    students = students + 1

print(i)
print(students)
