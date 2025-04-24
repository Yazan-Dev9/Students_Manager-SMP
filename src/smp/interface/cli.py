import getpass
from datetime import date
from app.user import User
from app.managment import Managment
from app.role import Role, RoleName
from modules.teacher import Teacher
from modules.person import Gender
from modules.student import Student
from modules.classRoom import ClassRoom

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
            "date": birth_date,
            "address": address,
            "phone": phone_number,
        }

    return info

def get_teacher_info():
    info = get_info()
    email = input("Enter email: -> ")
    public_number = input("Enter public number: -> ")

    teacher_info = {"email": email,
                    "public": public_number
                }

    info.update(teacher_info)
    
    return info

def set_info(obj, info):
    obj.set_name(str(info.get("name")))
    obj.set_mother_name(str(info.get("mother")))
    obj.set_gender(str(info.get("gender")))
    obj.set_date_of_birth(date.fromisoformat(str(info.get("date"))))
    obj.set_address(str(info.get("address")))
    obj.set_phone_number(str(info.get("phone")))

def add_teacher():
    print("Add Teacher")

    teacher = Teacher()

    info = get_teacher_info()

    set_info(teacher,info)

    teacher.set_email(str(info.get("email")))
    teacher.set_public_number(str(info.get("public")))

    teacher.save()

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

    room.save()

    print("Class Added Successfully")

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

def add_attendance():
    print("Add Attendance")
    st = manager.get_student_by_name("Yazan Khdaj")
    print(st.get_name())

def add_role():
    print("Add Role")
    name = input("Enter role name: -> ")

    manager.save_role(Role(name.lower()))
    
    print("Role Added Successfully")

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
                print("Add Subject")
                break
            case 7:
                print("Add Exam")
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

