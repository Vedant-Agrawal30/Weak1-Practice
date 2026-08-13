# Problem 2: Student Marks and Grade Analyzer
# Take the student’s name and five subject marks from the user.

# Store the marks inside a list.

# Calculate:

# Total Marks
# Average Marks
# Highest Mark
# Lowest Mark
# Number of Subjects Passed
# Number of Subjects Failed
# A student passes a subject when the mark is 40 or above.

# Determine the final grade using the average:

# Average 90 or above  → A
# Average 75 to 89     → B
# Average 60 to 74     → C
# Average 40 to 59     → D
# Average below 40     → F
# Display all marks that are greater than the average.

print("Student Marks and Grade Analyzer")

name = input("Enter the student's name: ")
marks = []
for i in range(5):
    mark = float(input(f"Enter the mark for subject {i + 1}: "))
    marks.append(mark)

total_marks = sum(marks)
average_marks = total_marks / len(marks)
highest_mark = max(marks)
lowest_mark = min(marks)

passed_subjects = sum(1 for mark in marks if mark >= 40)
failed_subjects = len(marks) - passed_subjects

if average_marks >= 90:
    grade = "A"
elif average_marks >= 75:
    grade = "B"
elif average_marks >= 60:
    grade = "C"
elif average_marks >= 40:
    grade = "D"
else:
    grade = "F"

greater_than_average = [mark for mark in marks if mark > average_marks]

print(f"\nStudent: {name}")
print(f"Total Marks: {total_marks}")
print(f"Average Marks: {average_marks:.2f}")
print(f"Highest Mark: {highest_mark}")
print(f"Lowest Mark: {lowest_mark}")
print(f"Number of Subjects Passed: {passed_subjects}")
print(f"Number of Subjects Failed: {failed_subjects}")
print(f"Final Grade: {grade}")
print(f"Marks Greater Than Average: {greater_than_average}")