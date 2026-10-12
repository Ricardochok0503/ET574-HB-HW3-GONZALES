
students = []
gpas = []

for i in range(25):
    name = input(f"Enter the name of student {i + 1}: ")
    gpa = float(input(f"Enter the GPA of {name}: "))

    students.append(name)
    gpas.append(gpa)

print("\nStudents and their GPAs:")

for i in range(25):
    print(f"Student: {students[i]}, GPA: {gpas[i]}")
