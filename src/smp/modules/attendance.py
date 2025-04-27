from datetime import date
from enum import Enum
from modules.student import Student

class Status(Enum):
    ''''''
    PRESENT = "Present"
    ABSENT = "Absent"
    LATE = "Late"
    @classmethod
    def get_all_status(cls):
        return [cls.PRESENT, cls.ABSENT, cls.LATE]


class Attendance:
    ''''''
    def __init__(self,status: str = "", id: int = 0):
        self.__id: int = id
        self.__status: str = status
        self.__date : date
        self.__student: Student

    @property
    def get_id(self):
        return self.__id

    @property
    def get_status(self):
        return self.__status

    def set_status(self, status: str):
        self.__status = status

    @property
    def get_date(self) -> date:
        return self.__date

    def set_date(self, date: date):
        self.__date = date

    @property
    def get_student(self) -> Student:
        return self.__student

    def set_student(self, student: Student):
        self.__student = student
