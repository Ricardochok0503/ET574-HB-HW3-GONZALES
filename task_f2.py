
students = []
gpas = []

# Read student names and GPAs from the file
file = open("students.txt", "r")

for line in file:
    data = line.strip().split(",")

    student = data[0]
    gpa = float(data[1])

    students.append(student)
    gpas.append(gpa)

file.close()

# Calculate the average GPA
total = 0

for gpa in gpas:
    total = total + gpa

average = total / len(gpas)

print("Average GPA:", round(average, 2))

# Print students above the average
print("\nStudents above average:")

for i in range(len(students)):
    if gpas[i] > average:
        print(students[i], "-", gpas[i])

# Predict scholarship winners
# Assumption: students with a GPA of 3.5 or higher
# are predicted to earn a scholarship.

print("\nPredicted scholarship winners:")

for i in range(len(students)):
    if gpas[i] >= 3.5:
        print(students[i], "-", gpas[i])
