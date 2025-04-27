import getpass
from datetime import date

from app.user import User
from app.role import Role, RoleName
from app.management import Management
from modules.teacher import Teacher
from modules.person import Gender
from modules.student import Student
from modules.classRoom import ClassRoom
from modules.subject import Subject
from modules.exam import Exam, ExamType
from modules.attendance import Attendance, Status

import pudb


manager = Management()


def login():

    print("Login Page")

    user = User()
    while True:
        user_name = input("Enter User Name: -> ")
        password = getpass.getpass("Enter your password: -> ")

        result = manager.get_user(user_name, password)

        if result:
            user.set_user_name(user_name)
            user.set_password(password)
            user.set_name(result[0][1])

            role = manager.get_role_by_id(result[0][4])

            user.set_role(Role(role[0][1], str(role[0][0])))

            return user
        else:
            print("User not found")


def add_user():
    print("Add User")

    name = input("Enter your name: -> ")
    user_name = input("Enter user name: -> ")
    admin = input("Is User Admin yes/no (no): -> ")

    while True:
        password = getpass.getpass("Enter your password: -> ")
        confirm_password = getpass.getpass("Confirm your password: -> ")

        if password == confirm_password:
            new_user = User()
            new_user.set_user_name(user_name)
            new_user.set_password(password)
            new_user.set_name(name)

            if admin.lower() == "yes":
                new_user.set_role(Role(RoleName.ADMIN.value))

            manager.save_user(new_user)

            print("User Added Successfully")
            break
        else:
            print("Password not match")


def get_info():
    name = input("Enter full name: -> ")
    mother = input("Enter mother name: -> ")

    gender = ""
    while not (
        gender.lower() == Gender.MALE.value or gender.lower() == Gender.FEMALE.value
    ):
        gender = input("Enter gender (Male/Female): -> ")

    while True:
        birth_date = input("Enter birth date (YYYY-MM-DD): -> ")
        try:
            date.fromisoformat(birth_date)
            break
        except ValueError as error:
            continue

    address = input("Enter address: -> ")
    phone_number = input("Enter phone number: -> ")

    info = {
        "name": name,
        "mother": mother,
        "gender": gender,
        "date": birth_date,
        "address": address,
        "phone": phone_number,
    }

    return info


def get_all_teachers_info():
    info = get_info()
    email = input("Enter email: -> ")
    public_number = input("Enter public number: -> ")

    all_teachers_info = {"email": email, "public": public_number}

    info.update(all_teachers_info)

    return info


def set_info(obj, info):
    obj.set_name(str(info.get("name")))
    obj.set_mother_name(str(info.get("mother")))
    obj.set_gender(str(info.get("gender")))
    obj.set_date_of_birth(str(info.get("date")))
    obj.set_address(str(info.get("address")))
    obj.set_phone_number(str(info.get("phone")))


def add_teacher():
    print("Add Teacher")

    teacher = Teacher()

    info = get_all_teachers_info()

    set_info(teacher, info)

    teacher.set_email(str(info.get("email")))
    teacher.set_public_number(str(info.get("public")))

    manager.save_teacher(teacher)

    print("Teacher Added Successfully")


def get_classes_list() -> list[ClassRoom]:
    classes: list[ClassRoom] = []

    all_classes = manager.get_all_classes()

    for all_classes_info in all_classes:
        class_room = ClassRoom(all_classes_info[1], all_classes_info[0])
        class_room.set_division(all_classes_info[2])
        class_room.set_capacity(all_classes_info[3])

        classes.append(class_room)

    return classes

def get_students_in_class(class_id :int) -> list[Student]:
    students: list[Student] = []

    all_students = manager.get_students_by_class(class_id)

    for students_info in all_students:
        student = Student(students_info[3], students_info[0])
        student.set_mother_name(students_info[4])
        student.set_gender(students_info[5])
        student.set_date_of_birth(students_info[6])
        student.set_address(students_info[7])
        student.set_phone_number(students_info[8])

        students.append(student)

    return students


def get_teachers_list() -> list[Teacher]:
    teachers: list[Teacher] = []
    all_teachers = manager.get_all_teachers()

    for all_teachers_info in all_teachers:
        teacher = Teacher( all_teachers_info[1],all_teachers_info[0])
        teacher.set_mother_name(all_teachers_info[2])
        teacher.set_gender(all_teachers_info[3])
        teacher.set_public_number(all_teachers_info[4])
        teacher.set_date_of_birth(all_teachers_info[5])
        teacher.set_address(all_teachers_info[6])
        teacher.set_phone_number(all_teachers_info[7])
        teacher.set_email(all_teachers_info[8])

        teachers.append(teacher)

    return teachers


def get_subjects_list() -> list[Subject]:
    subjects: list[Subject] = []

    all_subjects = manager.get_all_subjects()

    for all_subjects_info in all_subjects:
        subject = Subject(all_subjects_info[1], all_subjects_info[0])
        teacher = manager.get_teacher_by_id(all_subjects_info[2])
        subject.set_teacher(Teacher(teacher.get_name, teacher.get_id))
        class_room = manager.get_class_by_id(all_subjects_info[3])
        subject.set_class(ClassRoom(class_room.get_name, class_room.get_id))

        subjects.append(subject)

    return subjects


def add_student():
    print("Add Student")

    student = Student()

    info = get_info()

    set_info(student, info)

    classes = get_classes_list()
    ids = [0]

    while True:
        print("Choose Class")

        for class_data in classes:
            print(f"{class_data.get_id} - {class_data.get_name.capitalize()} - number {class_data.get_division}")
            ids.append(class_data.get_id)

        print("n - Create new class")
        choose = input("Enter choose number: -> ")

        if choose.isdigit() and int(choose) in ids:
            break
        elif choose.lower() == "n":
            break

    if choose == "n":
        add_class_room()
        id = ids[-1] + 1
    else:
        id = int(choose)

    class_info = manager.get_class_by_id(id)

    student.set_class(ClassRoom(class_info.get_name, class_info.get_id))

    manager.save_student(student)

    print("Student Added Successfully")


def add_class_room():
    print("Add Class Room")
    room = ClassRoom()

    room.set_name(input("Enter class name: -> "))

    capacity = ""
    while not capacity.isdigit():
        capacity = input("Enter class capacity of students: -> ")

    room.set_capacity(int(capacity))

    division = ""
    while not division.isdigit():
        division = input("Enter class division: -> ")

    room.set_division(int(division))

    manager.save_class_room(room)

    print("Class Added Successfully")


def add_attendance():
    print("Add Attendance")
    
    classes = get_classes_list()

    ids = [0]

    while True:
        print("Choose Class")

        for class_data in classes:
            print(f"{class_data.get_id} - {class_data.get_name.capitalize()} - number {class_data.get_division}")
            ids.append(class_data.get_id)

        choose = input("Enter choose number: -> ")

        if choose.isdigit() and int(choose) in ids:
            break

    ids = [0]

    students = get_students_in_class(int(choose))

    for student in students:
        print(f"{student.get_id} - {student.get_name.capitalize()}")
        
        while True:
            print("Choose Status")

            for i, status in enumerate(Status.get_all_status(), start=1):
                print(f"{i} - {status.value}")
                ids.append(i)
            
            choose = input("Enter choose number: -> ")

            if choose.isdigit() and int(choose) in ids:
                break
        
        attendance = Attendance()

        match int(choose):
            case 1:
                attendance.set_status(Status.PRESENT.value)
            case 2:
                attendance.set_status(Status.ABSENT.value)
            case 3:
                attendance.set_status(Status.LATE.value)

        while True:
            attendance_date = input("Enter exam date (YYYY-MM-DD): -> ")
            try:
                date.fromisoformat(attendance_date)
                break
            except ValueError:
                continue
        
        attendance.set_student(student)
        attendance.set_date(date.fromisoformat(attendance_date))

        manager.save_attendance(attendance)


def add_role():
    print("Add Role")
    name = input("Enter role name: -> ")

    manager.save_role(Role(name.lower()))

    print("Role Added Successfully")


def add_subject():
    print("Add Subject")

    subject = Subject()
    ids = [0]

    subject.set_name(input("Enter subject name: -> "))

    teachers = get_teachers_list()

    while True:
        print("Choose Teacher")

        for teacher_data in teachers:
            print(f"{teacher_data.get_id} - {teacher_data.get_name.capitalize()}")
            ids.append(teacher_data.get_id)

        print("n - Create new teacher")
        choose = input("Enter choose number: -> ")

        if choose.isdigit() and int(choose) in ids:
            break
        elif choose.lower() == "n":
            break

    if choose == "n":
        add_teacher()
        id = ids[-1] + 1
    else:
        id = int(choose)

    teacher_info = manager.get_teacher_by_id(id)

    classes = get_classes_list()

    ids = [0]

    while True:
        print("Choose Class")

        for class_data in classes:
            print(f"{class_data.get_id} - {class_data.get_name.capitalize()} - number {class_data.get_division}")
            ids.append(class_data.get_id)

        print("n - Create new class")
        choose = input("Enter choose number: -> ")

        if choose.isdigit() and int(choose) in ids:
            break
        elif choose.lower() == "n":
            break

    if choose == "n":
        add_class_room()
        id = ids[-1] + 1
    else:
        id = int(choose)

    class_info = manager.get_class_by_id(id)

    subject.set_teacher(Teacher(teacher_info.get_name, teacher_info.get_id))

    subject.set_class(ClassRoom(class_info.get_name, class_info.get_id))

    subject.set_description(input("Enter description (defult): -> "))

    manager.save_subject(subject)

    print("Subject Added Successfully")


def add_exam():
    print("Add Exam")

    exam = Exam()
    ids = [0]

    while True:
        for i, type in enumerate(ExamType.get_all_types(), start=1):
            print(f"{i} - {type.value}")

        match int(input("Enter exam type (1,2,3): ->")):
            case 1:
                exam.set_type(ExamType.FINAL.value)
                break
            case 2:
                exam.set_type(ExamType.MIDTERM.value)
                break
            case 3:
                exam.set_type(ExamType.QUIZ.value)
                break
            case _:
                print("Faild input")
                continue

    classes = get_classes_list()

    while True:
        print("Choose Class")

        for class_data in classes:
            print(f"{class_data.get_id} - {class_data.get_name.capitalize()}")
            ids.append(class_data.get_id)

        print("n - Create new class")
        choose = input("Enter choose number: -> ")

        if choose.isdigit() and int(choose) in ids:
            break
        elif choose.lower() == "n":
            break

    if choose == "n":
        add_class_room()
        id = ids[-1] + 1
    else:
        id = int(choose)

    class_info = manager.get_class_by_id(id)

    subjects = get_subjects_list()

    ids = [0]

    while True:
        print("Choose Subjects")

        for subject_data in subjects:
            print(f"{subject_data.get_id} - {subject_data.get_name.capitalize()}")
            ids.append(subject_data.get_id)

        print("n - Create new subject")
        choose = input("Enter choose number: -> ")

        if choose.isdigit() and int(choose) in ids:
            break
        elif choose.lower() == "n":
            break

    if choose == "n":
        add_subject()
        id = ids[-1] + 1
    else:
        id = int(choose)

    subject_info = manager.get_subject_by_id(id)

    while True:
        exam_date = input("Enter exam date (YYYY-MM-DD): -> ")
        try:
            date.fromisoformat(exam_date)
            break
        except ValueError:
            continue

    exam.set_subject(Subject(subject_info.get_name, subject_info.get_id))
    exam.set_class(ClassRoom(class_info.get_name, class_info.get_id))
    exam.set_date(date.fromisoformat(exam_date))
    exam.set_description(input("Enter description (defult): -> "))

    manager.save_exam(exam)

    print("Exam Added Successfully")


def show_classes():
    classes = get_classes_list()
    print("="*30)
    for class_data in classes:
        print(f"ID: {class_data.get_id} - Name: {class_data.get_name} - Division: {class_data.get_division} - Capacity: {class_data.get_capacity}")
        print("="*30)


def show_subjects():
    subjects = get_subjects_list()

    print("="*30)
    for subject_data in subjects:
        print(f"ID: {subject_data.get_id} Subject Name: {subject_data.get_name}")
        teacher = manager.get_teacher_by_id(int(subject_data.get_id))
        print(f"ID: {teacher.get_id} - Teacher Name: {teacher.get_name}")
        class_room = manager.get_class_by_id(int(subject_data.get_class.get_id))
        print(f"ID: {class_room.get_id} - Class Name: {class_room.get_name } - Division: {class_room.get_division}")
        print("="*30)


def admin_menu_board():
    print("1. Add User")
    print("2. Add Teacher")
    print("3. Add Student")
    print("4. Add Class Room")
    print("5. Add Attendance")
    print("6. Add Subject")
    print("7. Add exam")
    print("8. Add Exam Result")
    print("9. Add Time Table")
    print("10. Add Role")
    print("11. show classes")
    print("12. show subjects")
    print("0. Exit")


def admin():
    while True:
        admin_menu_board()

        match int(input("Enter Choose: -> ")):
            case 1:
                add_user()
                
            case 2:
                add_teacher()
                
            case 3:
                add_student()
                
            case 4:
                add_class_room()
                
            case 5:
                add_attendance()
                
            case 6:
                add_subject()
                
            case 7:
                add_exam()
                
            case 8:
                print("Add Exam Result")
                
            case 9:
                print("Add Time Table")
                
            case 10:
                add_role()
            
            case 11:
                show_classes()
            
            case 12:
                show_subjects()

            case 0:
                print("EXIT")
                exit(0)
            case _:
                print("Faild Input")
                continue


def main():
    print("Welcome To SMP")

    user = login()

    if user.is_admin():
        print(f"Welcome Manager {user.get_name()}")
        admin()
    else:
        print("Welcome Gest")
