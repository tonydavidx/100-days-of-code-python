students_heights = input('Input a list of Student heights: ').split()

# this for loop convers list inputs from string to integer
for n in range(0, len(students_heights)):
    students_heights[n] = int(students_heights[n])

print(students_heights)

students = 0

heights_sum = 0

for heights in students_heights:
    heights_sum = heights_sum + heights
    students = students + 1

average_height = heights_sum / students
round(average_height)

print(f"Sum of students heights: {heights_sum}")
print(f"number of students: {students}")
print(f"average students height: {average_height}")
