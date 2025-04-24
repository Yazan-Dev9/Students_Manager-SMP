from db.connection import DatabaseConnection
from modules.student import Student
from app.user import User
from app.role import Role

class Managment:

    def __init__(self):
        self.__db = DatabaseConnection("./src/smp/interface/storage/data/school.db")

    def get_student_by_name(self, name) -> Student:
        result = self.__db.execute_query("SELECT * FROM Student WHERE full_name = ?",(name,))
        
        student = Student(result[0][0])
        student.set_name(result[0][3])
        student.set_mother_name(result[0][4])
        student.set_gender(result[0][4])
        student.set_date_of_birth(result[0][6])
        student.set_address(result[0][7])
        
        return student

    def save_student(self, student: Student):
        self.__db.execute_query("INSERT INTO student (full_name,mother,gender,address,phone,date_of_birth) VALUES (?,?,?,?,?,?)",(student.get_name(),student.get_mother_name(),student.get_gender(),student.get_address(),student.get_phone_number(),student.get_date_of_birth()))
        self.__db.commit()
        self.__db.close()

    def save_user(self, user: User):
        role = self.get_role_by_name(user.get_role().get_name())
        user.get_role().set_id(role[0][0])
        self.__db.execute_query("INSERT INTO User (full_name,username,password,role_id) VALUES (?,?,?,?)",(user.get_name,user.get_user_name(),user.get_password(),user.get_role().get_id()))
        self.__db.commit()
        self.__db.close()

    def get_user(self, user_name, password):
        result = self.__db.execute_query("SELECT * FROM User WHERE username = ? AND password = ?",(user_name, password))
        return result

    def save_role(self, role: Role):
        self.__db.execute_query("INSERT INTO Role (role_name) VALUES (?,)",(role.get_name(),))
        self.__db.commit()
        self.__db.close()

    def get_role_by_name(self, name):
        role = self.__db.execute_query("SELECT * FROM Role WHERE role_name = ?",(name,))
        return role
    
    def get_role_by_id(self, id: int):
        role = self.__db.execute_query("SELECT * FROM Role WHERE role_id = ?",(id,))
        return role
