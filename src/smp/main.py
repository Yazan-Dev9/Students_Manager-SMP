from datetime import date
from person import Gender
from classManager import ClassManager
from classRoom import ClassRoom
from student import Student
from studentManager import StudentManager

def main():
    student_manager = StudentManager()

    class_manager = ClassManager()

    room  = ClassRoom("room 1")
    room1 = ClassRoom("room 2")

    student = Student("Alice")
    student.set_gender(Gender.MALE)
    student.set_address("123 Main St")
    student.set_phone_number("555-1234")
    student.set_email("alice@example.com")
    student.set_date_of_birth(date(1998, 5, 15))
    student.add_grade(55)
    student.add_grade(90)

    student1 = Student("yazan")
    student1.set_gender(Gender.MALE)
    student1.set_address("Syria")
    student1.set_phone_number("0996125895")
    student1.set_email("yazan@example.com")
    student1.set_date_of_birth(date(2000, 4, 7))
    student1.add_grade(87)
    student1.add_grade(95)

    student2 = Student("mary")
    student2.set_gender(Gender.FEMALE)
    student2.set_address("Egpt")
    student2.set_phone_number("110335454534")
    student2.set_email("mary@example.com")
    student2.set_date_of_birth(date(2001, 1, 13))
    student2.add_grade(45)
    student2.add_grade(70)


    class_manager.create_class(room)
    class_manager.create_class(room1)

    class_manager.add_student_to_class(student, room)
    class_manager.add_student_to_class(student1, room)
    class_manager.add_student_to_class(student2, room1)

    student_manager.add_student(student)
    student_manager.add_student(student1)
    student_manager.add_student(student2)



    # Add grades to students
    student_manager.get_student_by_name("Alice").add_grade(95) # type: ignore

    #  Get all students
    all_students = student_manager.get_students()
    print("All Students:")
    for student in all_students:
        print(f"{student}, Average Grade: {student.get_average()}")
        print("--------------------------------")
        print("Grades:")
        for grade in student.get_grades():
            print(f"Grade: {grade}")
            print("--------------------------------")
    print("=======================================")

    # Get students by name
    alice = student_manager.get_student_by_name("Alice")
    if alice:
        print("Student Found:")
        print(f"Name: {alice.get_name()}, Age: {alice.get_age()}, Average Grade: {alice.get_average()}")
        print("Grades:")
        for grade in alice.get_grades():
            print(f"Grade: {grade}")
            print("--------------------------------")
    else:
        print("Student not found.") 
        print("--------------------------------")
    print("=======================================")

    # Get students by average grade
    students_by_grade = student_manager.get_students_by_average(80)
    if students_by_grade:
        print("Students by Average Grade:")
        for student in students_by_grade:
            print(f"Name: {student.get_name()}, Age: {student.get_age()}, Average Grade: {student.get_average()}")
            print("Grades:")
            for grade in student.get_grades():
                print(f"Grade: {grade}")
                print("--------------------------------")
    else:
        print("No students found for the given average grade.")
        print("--------------------------------")
    print("=======================================")

    students_by_class = student_manager.get_students_by_class(room.get_class_name())
    if students_by_class:
        print("found students in class")
        for student in students_by_class:
            print(student.get_name())
    else:
        print("No students found for the given class.")
    print("--------------------------------")