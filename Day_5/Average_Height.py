# Prompt the user to input a list of student heights

student_heights = input("Enter the heights of students (cm): e.g 150, 200, 300, 400 \n").split(',')
for height in range(0, len(student_heights)):
    student_heights[height] = int(student_heights[height])

total_height = 0
for num in student_heights:
    total_height += num

num_student = 0
for num in student_heights:
    num_student += 1

average_height = int(round(total_height / num_student, 0))
print(f"total height = {total_height}cm")
print(f"number of students = {num_student}")
print(f"average height = {average_height:.2f}cm")