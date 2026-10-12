
students = ["Jon", "Kim", "Lee", "Sara", "Miko",
            "Lin", "Toby", "Ben", "Mark", "Xia"]

gpas = [3.25, 2.25, 2.30, 4.00, 1.90,
        2.10, 2.89, 2.75, 2.34, 3.53]

# Calculate the average GPA
total = sum(gpas)
average = total / len(gpas)

print("Average GPA:", round(average, 2))

# Print students with above-average GPAs
print("\nStudents above average:")

for i in range(len(students)):
    if gpas[i] > average:
        print(students[i], "-", gpas[i])

# Predict scholarship eligibility
# Assume a GPA of 3.50 or higher qualifies
print("\nPredicted scholarship students:")

for i in range(len(students)):
    if gpas[i] >= 3.50:
        print(students[i], "-", gpas[i])
