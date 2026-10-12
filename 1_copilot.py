# list of three students named Jon, Kim and Lee
students = ["Jon", "Kim", "Lee"]
students.append("Sara")
students.append("Miko")

# change Jon to John
students[0] = "John"

# function to print ‘Hi name’ for each student in the list and total number of students
def greet_students(student_list):
    print(f"Total students: {len(student_list)}")
    for student in student_list:
        print(f"Hi {student}")

# call the function
greet_students(students)