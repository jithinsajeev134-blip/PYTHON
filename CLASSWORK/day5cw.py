python_students = {"Alice", "Bob", "Charlie"}
data_science_students = {"Bob", "David", "Eve"}

python_students.add("Frank")

data_science_students.remove("Eve")

both_courses = python_students & data_science_students
print("Students in both courses:", both_courses)

only_python = python_students - data_science_students
print("Students only in Python:", only_python)
all_students = python_students | data_science_students
print("All students in either course:", all_students)

course_counts = {
    "Python": len(python_students),
    "Data Science": len(data_science_students)
}

for course, count in course_counts.items():
    print(f"Course: {course}, Students: {count}")

expected_growth = {course: count * 2 for course, count in course_counts.items()}
print("Expected growth:", expected_growth)