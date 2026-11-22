subjects = ["Physics", "Chemistry", "Maths", "Biology", "English"]
marks = {}

for subject in subjects:
    score = float(input(f"Enter marks for {subject}: "))
    marks[subject] = score

total = sum(marks.values())
percentage = total / len(subjects)

highest = max(marks, key=marks.get)
lowest = min(marks, key=marks.get)

# Grade system
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "Needs Improvement"

# Performance message
if percentage >= 90:
    message = "Excellent performance!"
elif percentage >= 70:
    message = "Good performance!"
else:
    message = "Keep practicing!"

# Display report
print("\n===== STUDENT REPORT =====")

for subject, score in marks.items():
    print(subject, ":", score)

print("Total Marks:", total)
print("Percentage:", percentage, "%")
print("Grade:", grade)
print("Highest Subject:", highest)
print("Lowest Subject:", lowest)
print(message)