# This program takes a list of scores and returns the highest score

# Input a list of student scores
student_scores = input("Enter the various scores for each student: e.g 15, 23, 29, 34 \n").split(',')
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Write your code below this row 👇
max_score = 0
for num in student_scores:
  if num > max_score:
    max_score = num
print(f"The highest score in the class is: {max_score}")