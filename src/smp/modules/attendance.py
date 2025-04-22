from datetime import date
from enum import Enum
from student import Student

class Status(Enum):
    ''''''
    PRESENT = "Present"
    ABSENT = "Absent"
    LATE = "Late"
    @classmethod
    def get_all_types(cls):
        return [cls.PRESENT, cls.ABSENT, cls.LATE]


class Attendance:
    ''''''
    def __init__(self,status: str, id: str = ""):
        self.__id: str = id
        self.__status: str = status
        self.__date : date
        self.__student: Student

    def get_id(self):
        return self.__id

    def get_status(self):
        return self.__status

    def set_status(self, status: str):
        self.__status = status

    def get_date(self) -> date:
        return self.__date

    def set_date(self, date: date):
        self.__date = date

    def get_student(self) -> Student:
        return self.__student

    def set_student(self, student: Student):
        self.__student = student
