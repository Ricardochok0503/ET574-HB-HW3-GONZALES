
# Store student names and GPAs in two lists
students = ["Jon", "Kim", "Lee", "Sara", "Miko",
            "Lin", "Toby", "Ben", "Mark", "Xia"]

gpas = [3.25, 2.25, 2.30, 4.00, 1.90,
        2.10, 2.89, 2.75, 2.34, 3.53]

# Calculate the average GPA
total = sum(gpas)
average = total / len(gpas)

print("Average GPA:", round(average, 2))

# Print students above the average GPA
print("\nStudents above average:")

for i in range(len(students)):
    if gpas[i] > average:
        print(students[i], gpas[i])

# Predict scholarship eligibility
# Based on the examples, a GPA of 2.75 or higher qualifies
print("\nStudents predicted to earn a scholarship:")

for i in range(len(students)):
    if gpas[i] >= 2.75:
        print(students[i], gpas[i], "earned a scholarship.")
