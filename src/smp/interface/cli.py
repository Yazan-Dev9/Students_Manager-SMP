import getpass
from app.user import User

def main():
    # TODO login to system User Name admin password 123

    print("Welcome To SMP")
    print("Login Page")

    user = User()

    user_name = input("Enter User Name: -> ")
    password = getpass.getpass("Enter your password: -> ")

    user.set_user_name(user_name)
    user.set_password(password)

    if(user.is_admin()):
        print(f"Welcome Manager {user.get_name()}")
        while(True):
            print("1. Add User")
            print("2. Add Teacher")
            print("3. Add Subject")
            print("4. Add Class Room")
            print("5. Add Attendance")
            print("6. Add Student")
            print("7. Add exam")
            print("8. Add Exam Result")
            print("9. Add Time Table")
            print("0. Exit")

            match int(input("Enter Choose: -> ")):
                case 1:
                    print("Add User")
                    user_name = input("Enter user name: -> ")
                    name = input("Enter your name: -> ")
                    password = getpass.getpass("Enter your password: -> ")
                    confirm_password = getpass.getpass("Confirm your password: -> ")
                    admin = input("Is User Admin yes/no (no): -> ")
                    
                    if password == confirm_password:
                        new_user = User()
                        new_user.set_user_name(user_name)
                        new_user.set_password(password)
                        new_user.set_name(name)
                        
                        if admin.lower() == "yes":
                            new_user.set_admin()
                        new_user.save()
                        print("User Added Successfully")
                    else:
                        print("Password not match")
                        break
                case 2:
                    print("Add Teacher")
                    break
                case 3:
                    print("Add Subject")
                    break
                case 4:
                    print("Add Class Room")
                    break
                case 5:
                    print("Add Attendance")
                    break
                case 6:
                    print("Add Student")
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
                case 0:
                    print("EXIT")
                    exit(0)
                case _:
                    print("Faild Input")
                    continue
    else:
        print("Welcome Gest")

