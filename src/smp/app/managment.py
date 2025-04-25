from db.connection import DatabaseConnection
from app.user import User
from app.role import Role
from modules.student import Student
from modules.classRoom import ClassRoom
from modules.subject import Subject
from modules.exam import Exam
from modules.teacher import Teacher

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
        self.__db.execute_query("INSERT INTO Student (full_name,mother,gender,address,phone,date_of_birth) VALUES (?,?,?,?,?,?)",(student.get_name(),student.get_mother_name(),student.get_gender(),student.get_address(),student.get_phone_number(),student.get_date_of_birth()))
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

    def save_class_room(self, class_room: ClassRoom):
        self.__db.execute_query("INSERT INTO Classroom (name,capacity) VALUES (?,?)",(class_room.get_name(), class_room.get_capacity()))
        self.__db.commit()
        self.__db.close()

    def get_all_teachers(self):
        teachers = self.__db.execute_query("SELECT * FROM Teacher")
        return teachers

    def save_subject(self, subject: Subject):
        self.__db.execute_query("INSERT INTO Subject (name,teacher_id,description) VALUES (?,?,?)",(subject.get_name(), subject.get_teacher().get_id,subject.get_description()))
        self.__db.commit()
        self.__db.close()

    def get_teacher_by_id(self,id: int):
        teacher = self.__db.execute_query("SELECT * FROM Teacher WHERE teacher_id = ?",(id,))
        return teacher
    
    def save_teacher(self, teacher: Teacher):
        self.__db.execute_query("INSERT INTO Teacher (full_name,mother,gender,address,phone,date_of_birth,public_number,email) VALUES (?,?,?,?,?,?)",(teacher.get_name(),teacher.get_mother_name(),teacher.get_gender(),teacher.get_address(),teacher.get_phone_number(),teacher.get_date_of_birth(),teacher.get_public_number(),teacher.get_email()))
        self.__db.commit()
        self.__db.close()

    def save_exam(self, exam: Exam):
        self.__db.execute_query("INSERT INTO Exam (type,exam_date,description,subject_id) VALUES (?,?,?,?)",(exam.get_type(), exam.get_date(), exam.get_description(), exam.get_subject().get_id()))
        self.__db.commit()
        self.__db.close()