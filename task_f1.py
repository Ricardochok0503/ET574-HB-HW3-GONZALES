
students = []
gpas = []

# Read student data from the file
with open("students.txt", "r") as file:
    for line in file:
        data = line.strip().split(",")

        student = data[0]
        gpa = float(data[1])

        students.append(student)
        gpas.append(gpa)

# Compute the average GPA
average_gpa = sum(gpas) / len(gpas)

print("Average GPA:", round(average_gpa, 2))

# Print students above average
print("\nStudents above average:")
for i in range(len(students)):
    if gpas[i] > average_gpa:
        print(students[i], "-", gpas[i])

# Predict scholarship recipients
print("\nPredicted scholarship recipients:")
for i in range(len(students)):
    if gpas[i] >= 3.5:
        print(students[i], "-", gpas[i])
