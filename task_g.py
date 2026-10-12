
students = ["Jon", "Kim", "Lee", "Sara", "Miko",
            "Lin", "Toby", "Ben", "Mark", "Xia"]

gpas = [3.25, 2.25, 2.30, 4.00, 1.90,
        2.10, 2.89, 2.75, 2.34, 3.53]

scholarship_students = ["Jake", "Markus", "Teri", "Leigh"]
scholarship_gpas = [2.75, 2.90, 3.15, 3.75]

# Calculate the average GPA
total = 0

for gpa in gpas:
    total = total + gpa

average = total / len(gpas)

print("Average GPA:", round(average, 2))

# Print students with above-average GPAs
print("\nStudents with above-average GPAs:")

for i in range(len(students)):
    if gpas[i] > average:
        print(students[i], gpas[i])

# Predict which students will earn a scholarship
print("\nPredicted scholarship students:")

for i in range(len(scholarship_students)):
    if scholarship_gpas[i] >= 3.0:
        print(scholarship_students[i], scholarship_gpas[i])
