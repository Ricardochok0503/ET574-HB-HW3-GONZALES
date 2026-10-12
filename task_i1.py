
students = {
    "Jon": {"GPA": 3.25, "Major": "Math"},
    "Kim": {"GPA": 2.25, "Major": "Biology"},
    "Lee": {"GPA": 2.30, "Major": "Math"},
    "Sara": {"GPA": 4.00, "Major": "Math"},
    "Miko": {"GPA": 1.90, "Major": "Math"},
    "Lin": {"GPA": 2.10, "Major": "Biology"},
    "Toby": {"GPA": 2.89, "Major": "Biology"},
    "Ben": {"GPA": 2.75, "Major": "Math"},
    "Mark": {"GPA": 2.34, "Major": "Math"},
    "Xia": {"GPA": 3.53, "Major": "Biology"}
}

# Calculate the average GPA
total_gpa = 0

for name in students:
    total_gpa = total_gpa + students[name]["GPA"]

average_gpa = total_gpa / len(students)

print("Average GPA:", round(average_gpa, 2))

# Print students above average
print("\nStudents above average:")

for name in students:
    if students[name]["GPA"] > average_gpa:
        print(name, students[name]["GPA"], students[name]["Major"])

# Predict scholarship eligibility
print("\nScholarship predictions:")

for name in students:
    gpa = students[name]["GPA"]
    major = students[name]["Major"]

    if gpa >= 3.5:
        scholarship = "earned a scholarship"
    elif major == "Biology" and gpa >= 2.5:
        scholarship = "earned a scholarship"
    elif gpa > average_gpa and major == "Biology":
        scholarship = "earned a scholarship"
    else:
        scholarship = "did not earn a scholarship"

    print(name, "-", scholarship)
