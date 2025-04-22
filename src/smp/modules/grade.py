from exam import Exam
from student import Student

class Grade:
    ''''''
    def __init__(self, score: float, exam: Exam, id: str = "" ):
        self.__id: str = id
        self.__exam: Exam = exam
        self.__score: float = score
        self.__student: Student

    def get_id(self):
        return self.__id

    def get_exam(self) -> Exam:
        return self.__exam

    def set_exam(self, exam: Exam):
        self.__exam = exam

    def get_score(self):
        return self.__score

    def set_score(self, score: float):
        self.__score = score

    def get_student(self) -> Student:
        return self.__student

    def set_student(self, student: Student):
        self.__student = student
