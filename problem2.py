name = input("Enter your name: ")
marks = []

for i in range(5):
    mark = int(input())
    marks.append(mark)

total = sum(marks)
avg = total/len(marks)
highest = max(marks)
lowest = min(marks)
print(name)
print(marks)
print(f"Total Marks: {total}")
print("Average Marks: ",avg)
print("Highest Marks: ",highest)
print("Lowest Marks: ",lowest)

count = 0

for mark in marks:
    if mark>=40:
        count = count+1
print(f"No of Passed Students: {count}")
failed = len(marks) - count
print(f"No of Failed Students: {failed}")

if avg>= 90:
    print("Grade: A")
elif avg >= 75:
    print("Grade: B")
elif avg >= 60:
    print("Grade: C")
elif avg >= 40:
    print("Grade: D")
else:
    print("Grade: F")

greater_marks = []

for mark in marks:
    if mark > avg:
        greater_marks.append(mark)

print("Greater then Average Marks: ",greater_marks)