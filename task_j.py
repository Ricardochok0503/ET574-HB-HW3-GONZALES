
import csv

students = {}

# Read student data from the CSV file
with open("students.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        name = row["name"]
        major = row["major"]
        gpa = float(row["gpa"])

        if 0.0 <= gpa <= 4.0:
            students[name] = {
                "major": major,
                "gpa": gpa
            }

# Calculate the average GPA
total_gpa = sum(student["gpa"] for student in students.values())
average_gpa = total_gpa / len(students)

print(f"Average GPA: {average_gpa:.2f}")

# Print all students above average
print("\nStudents above average:")

for name, student in students.items():
    if student["gpa"] > average_gpa:
        print(
            f"{name} - {student['major']} - "
            f"GPA: {student['gpa']:.2f}"
        )

# Predict scholarship eligibility
print("\nScholarship predictions:")

for name, student in students.items():
    major = student["major"]
    gpa = student["gpa"]

    # Prediction rule based on the provided examples
    if major == "Biology" or gpa >= 3.5:
        scholarship = "Earns a scholarship"
    else:
        scholarship = "Does not earn a scholarship"

    print(
        f"{name} - {major} - GPA: {gpa:.2f} - "
        f"{scholarship}"
    )
