import getpass
from datetime import date
from app.user import User
from app.managment import Managment
from app.role import Role, RoleName
from modules.teacher import Teacher
from modules.person import Gender
from modules.student import Student
from modules.classRoom import ClassRoom
from modules.subject import Subject
from modules.exam import Exam, ExamType

manager = Managment()

def login():

    print("Login Page")
    
    user = User()
    while(True):
        user_name = input("Enter User Name: -> ")
        password = getpass.getpass("Enter your password: -> ")
        
        result = manager.get_user(user_name, password)
        
        if(result):
            user.set_user_name(user_name)
            user.set_password(password)
            user.set_name(result[0][1])
            
            role = manager.get_role_by_id(result[0][4])
            
            user.set_role(Role(role[0][1],str(role[0][0])))
            
            return user
        else:
            print("User not found")

def add_user():
    print("Add User")
    
    name = input("Enter your name: -> ")
    user_name = input("Enter user name: -> ")
    admin = input("Is User Admin yes/no (no): -> ")

    while(True):
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
    while not (gender.lower() == Gender.MALE.value or gender.lower() == Gender.FEMALE.value):
        gender = input("Enter gender (Male/Female): -> ")

    while(True):
        birth_date = input("Enter birth date (YYYY-MM-DD): -> ")
        try:
            date.fromisoformat(birth_date)
            break
        except ValueError:
            continue

    address = input("Enter address: -> ")
    phone_number = input("Enter phone number: -> ")

    info = {"name": name,
            "mother": mother,
            "gender": gender,
            "date": date.fromisoformat(birth_date),
            "address": address,
            "phone": phone_number,
        }

    return info

def get_all_teachers_info():
    info = get_info()
    email = input("Enter email: -> ")
    public_number = input("Enter public number: -> ")

    all_teachers_info = {"email": email,
                        "public": public_number
                    }

    info.update(all_teachers_info)
    
    return info

def set_info(obj, info):
    obj.set_name(str(info.get("name")))
    obj.set_mother_name(str(info.get("mother")))
    obj.set_gender(str(info.get("gender")))
    obj.set_date_of_birth(date.fromisoformat(info.get("date")))
    obj.set_address(str(info.get("address")))
    obj.set_phone_number(str(info.get("phone")))

def add_teacher():
    print("Add Teacher")

    teacher = Teacher()

    info = get_all_teachers_info()

    set_info(teacher,info)

    teacher.set_email(str(info.get("email")))
    teacher.set_public_number(str(info.get("public")))

    manager.save_teacher(teacher)

    print("Teacher Added Successfully")

def add_student():
    print("Add Student")

    student =Student()

    info = get_info()

    set_info(student, info)

    manager.save_student(student)

    print("Student Added Successfully")

def add_class_room():
    print("Add Class Room")
    room = ClassRoom()

    room.set_name(input("Enter class name: -> "))

    capacity = ""
    while(not capacity.isdigit()):
        capacity = input("Enter class number: -> ")

    room.set_capacity(int(capacity))

    manager.save_class_room(room)

    print("Class Added Successfully")

def add_attendance():
    print("Add Attendance")
    st = manager.get_student_by_name("Yazan Khdaj")
    print(st.get_name())

def add_role():
    print("Add Role")
    name = input("Enter role name: -> ")

    manager.save_role(Role(name.lower()))
    
    print("Role Added Successfully")

def get_teachers_list() -> list[Teacher] :
    teacher = Teacher()
    teachers : list[Teacher] = []

    all_teachers = manager.get_all_teachers()

    for all_teachers_info in all_teachers:
        teacher.set_id(all_teachers_info[0])
        teacher.set_name(all_teachers_info[1])
        teacher.set_mother_name(all_teachers_info[2])
        teacher.set_date_of_birth(all_teachers_info[5])
        teacher.set_gender(all_teachers_info[3])
        teacher.set_address(all_teachers_info[6])
        teacher.set_phone_number(all_teachers_info[7])
        teacher.set_email(all_teachers_info[8])
        teacher.set_public_number(all_teachers_info[4])

        teachers.append(teacher)
    
    return teachers

def add_subject():
    print("Add Subject")
    
    subject = Subject()
    ids = []
    id = 0
    
    subject.set_name(input("Enter subject name: -> "))

    teachers = get_teachers_list()

    while True:
        print("Choose Teacher")

        for teacher_data in teachers:
            print(f"{teacher_data.get_id()} - {teacher_data.get_name().capitalize()}")
            ids.append(teacher_data.get_id())

        print("n - Create new Teacher")
        choose = input("Enter choose number: -> ")

        if choose.isdigit() or choose.lower() == "n":
            break
    
    if choose == "n":
        add_teacher()
        id = ids[-1] + 1
    else:
        id = int(choose)

    teacher_info = manager.get_teacher_by_id(id)

    subject.set_teacher(Teacher(teacher_info[1], teacher_info[0]))

    subject.set_description(input("Enter description (defult): -> "))

    manager.save_subject(subject)

    print("Subject Added Successfully")

def add_exam():
    print("Add Exam")

    exam = Exam()

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

    while(True):
        exam_date = input("Enter exam date (YYYY-MM-DD): -> ")
        try:
            date.fromisoformat(exam_date)
            break
        except ValueError:
            continue

    exam.set_date(date.fromisoformat(exam_date))
    exam.set_description(input("Enter description (defult): -> "))


    manager.save_exam(exam)

    print("Exam Added Successfully")

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
    print("0. Exit")

def admin():
    while(True):
        admin_menu_board()

        match int(input("Enter Choose: -> ")):
            case 1:
                add_user()
                break
            case 2:
                add_teacher()
                break
            case 3:
                add_student()
                break
            case 4:
                add_class_room()
                break
            case 5:
                add_attendance()
                break
            case 6:
                add_subject()
                break
            case 7:
                add_exam()
                break
            case 8:
                print("Add Exam Result")
                break
            case 9:
                print("Add Time Table")
                break
            case 10:
                add_role()
                break
            case 0:
                print("EXIT")
                exit(0)
            case _:
                print("Faild Input")
                continue

def main():
    # TODO login to system User Name admin password 123
    
    print("Welcome To SMP")
    
    user = login()
    
    if(user.is_admin()):
        print(f"Welcome Manager {user.get_name()}")
        admin()
    else:
        print("Welcome Gest")

