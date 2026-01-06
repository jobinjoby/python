
frontend_students = {"sanju", "varun", "sachin", "Dhoni"}
backend_students = {"varun", "rohit", "sanju", "bumrah"}
backend_students.add("abishek")
frontend_students.remove("Dhoni")
both_courses = frontend_students & backend_students
print("Students enrolled in both Frontend and Backend:", both_courses)
only_backend = backend_students - frontend_students
print("Students enrolled only in Backend:", only_backend)
unique_students = frontend_students | backend_students
print("Total number of unique students:", len(unique_students))
course_enrollment = {
    "Frontend": len(frontend_students),
    "Backend": len(backend_students)
}
for course, count in course_enrollment.items():
    print(f"{course} course has {count} students")
course_enrollment_with_fullstack = {
    course: count for course, count in course_enrollment.items()
}

course_enrollment_with_fullstack["Fullstack"] = (
    course_enrollment["Frontend"] + course_enrollment["Backend"]
)

print(course_enrollment_with_fullstack)


