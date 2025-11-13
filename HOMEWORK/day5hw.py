frontend_students = {"Asha", "Bala", "Chitra", "Dev"}
backend_students = {"Chitra", "Eshan", "Farah"}

backend_students.add("Gopal")

frontend_students.remove("Dev")

both_courses = frontend_students & backend_students
print("Students in both courses:", both_courses)

only_backend = backend_students - frontend_students
print("Students only in Backend:", only_backend)

unique_students = frontend_students | backend_students
print("Total unique students:", len(unique_students))

course_counts = {
    "Frontend": len(frontend_students),
    "Backend": len(backend_students)
}

for course, count in course_counts.items():
    print(f"Course: {course}, Students: {count}")

expanded_courses = {
    **course_counts,
    "Fullstack": sum(course_counts.values())
}
print("Expanded course dictionary:", expanded_courses)