print("Welcome to Average Height Calculator!")

student_heights = input(
    "Input a list of student heights, separated by a space: ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

sum = 0

for height in student_heights:
    sum += height

print(f"The average height is {round(sum / len(student_heights))}.")
