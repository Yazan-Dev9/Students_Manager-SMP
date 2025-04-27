from db.connection import DatabaseConnection
from app.user import User
from app.role import Role
from modules.student import Student
from modules.classRoom import ClassRoom
from modules.subject import Subject
from modules.exam import Exam
from modules.teacher import Teacher
from modules.attendance import Attendance



class Management:

    def __init__(self):
        self.__db = DatabaseConnection("./src/smp/interface/storage/data/school.db")

    def get_student_by_name(self, name: str) -> Student:
        result = self.__db.execute_query(
            "SELECT * FROM Student WHERE full_name = ?", (name,)
        )
        if not result:
            raise ValueError("Student not found")

        student_data = result[0]
        student = Student(student_data[3], student_data[0])
        student.set_mother_name(student_data[4])
        student.set_gender(student_data[5])
        student.set_date_of_birth(student_data[6])
        student.set_address(student_data[7])
        return student
    
    def get_students_by_class(self, class_id: int):
        students = self.__db.execute_query(
            "SELECT * FROM Student WHERE class_id = ?", (class_id,)
        )
        if not students:
            raise ValueError("Class not found or no students in class")
        
        return students

    def save_student(self, student: Student):
        self.__db.execute_query(
            """INSERT INTO Student (full_name, mother, gender, address, phone, date_of_birth, class_id)
                VALUES (?, ?, ?, ?, ?, ?, ?)""",
            (
                student.get_name,
                student.get_mother_name,
                student.get_gender,
                student.get_address,
                student.get_phone_number,
                student.get_date_of_birth,
                student.get_class.get_id,
            ),
        )
        self.__db.commit()

    def save_user(self, user: User):
        role = self.get_role_by_name(user.get_role().get_name())
        if not role:
            raise ValueError("Role not found")

        user.get_role().set_id(role[0][0])
        self.__db.execute_query(
            "INSERT INTO User (full_name, username, password, role_id) VALUES (?, ?, ?)",
            (
                user.get_name(),
                user.get_user_name(),
                user.get_password(),
                user.get_role().get_id(),
            ),
        )
        self.__db.commit()

    def get_user(self, user_name: str, password: str):
        result = self.__db.execute_query(
            "SELECT * FROM User WHERE username = ? AND password = ?",
            (user_name, password),
        )
        return result

    def save_role(self, role: Role):
        self.__db.execute_query(
            "INSERT INTO Role (role_name) VALUES (?)",
            (role.get_name(),),
        )
        self.__db.commit()

    def get_role_by_name(self, name: str):
        role = self.__db.execute_query(
            "SELECT * FROM Role WHERE role_name = ?", (name,)
        )
        return role

    def get_role_by_id(self, id: int):
        role = self.__db.execute_query("SELECT * FROM Role WHERE role_id = ?", (id,))
        return role

    def save_class_room(self, class_room: ClassRoom):
        self.__db.execute_query(
            "INSERT INTO Classroom (name, division, capacity) VALUES (?, ?, ?)",
            (class_room.get_name, class_room.get_division, class_room.get_capacity),
        )
        self.__db.commit()
    
    def save_attendance(self, attendance: Attendance):
        self.__db.execute_query(
            "INSERT INTO Attendance (student_id, date, status) VALUES (?, ?, ?)",
            (attendance.get_student.get_id, attendance.get_date, attendance.get_status),
        )
        self.__db.commit()

    def get_all_teachers(self):
        teachers = self.__db.execute_query("SELECT * FROM Teacher")
        return teachers

    def get_all_classes(self):
        classes = self.__db.execute_query("SELECT * FROM Classroom")
        return classes

    def get_all_subjects(self):
        subjectss = self.__db.execute_query("SELECT * FROM Subject")
        return subjectss

    def save_subject(self, subject: Subject):
        self.__db.execute_query(
            "INSERT INTO Subject (name, teacher_id, class_id , description) VALUES (?, ?, ?, ?)",
            (
                subject.get_name,
                subject.get_teacher.get_id,
                subject.get_class.get_id,
                subject.get_description
            ),
        )
        self.__db.commit()

    def get_teacher_by_id(self, id: int) -> Teacher:
        result = self.__db.execute_query(
            "SELECT * FROM Teacher WHERE teacher_id = ?", (id,)
        )
        if not result:
            raise ValueError("Teacher not found")

        teacher_data = result[0]
        teacher = Teacher(teacher_data[1],teacher_data[0])
        teacher.set_mother_name(teacher_data[2])
        teacher.set_gender(teacher_data[3])
        teacher.set_public_number(teacher_data[4])
        teacher.set_date_of_birth(teacher_data[5])
        teacher.set_address(teacher_data[6])
        teacher.set_phone_number(teacher_data[7])
        teacher.set_email(teacher_data[8])
        
        return teacher

    def get_class_by_id(self, id: int) -> ClassRoom:
        result = self.__db.execute_query(
            "SELECT * FROM Classroom WHERE classroom_id = ?", (id,)
        )
        if not result:
            raise ValueError("Class not found")

        class_data = result[0]
        class_room = ClassRoom(class_data[1], class_data[0])
        class_room.set_division(class_data[2])
        class_room.set_capacity(class_data[3])

        return class_room
    
    def get_subject_by_id(self, id: int) -> Subject:
        result = self.__db.execute_query(
            "SELECT * FROM Subject WHERE subject_id = ?", (id,)
        )
        if not result:
            raise ValueError("Class not found")

        subject_data = result[0]
        subject = Subject(subject_data[1], subject_data[0])

        return subject

    def save_teacher(self, teacher: Teacher):
        self.__db.execute_query(
            """INSERT INTO Teacher (full_name, mother, gender, address, phone, date_of_birth, public_number, email)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                teacher.get_name,
                teacher.get_mother_name,
                teacher.get_gender,
                teacher.get_address,
                teacher.get_phone_number,
                teacher.get_date_of_birth,
                teacher.get_public_number,
                teacher.get_email,
            ),
        )
        self.__db.commit()

    def save_exam(self, exam: Exam):
        self.__db.execute_query(
            "INSERT INTO Exam (type, exam_date, description, subject_id, class_id) VALUES (?, ?, ?, ?, ?)",
            (
                exam.get_type,
                exam.get_date,
                exam.get_description,
                exam.get_subject.get_id,
                exam.get_class.get_id,
            ),
        )
        self.__db.commit()