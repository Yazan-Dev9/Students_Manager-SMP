from datetime import date
from enum import Enum

class ExamType(Enum):
    ''''''
    MIDTERM = "Midterm"
    FINAL = "Final"
    QUIZ = "Quiz"
    @classmethod
    def get_all_types(cls):
        return [cls.MIDTERM, cls.FINAL, cls.QUIZ]

class Exam:
    ''''''
    def __init__(self, type: str, id: str = "" ):
        self.__id: str = id
        self.__type: str = type
        self.__date: date

    def get_id(self):
        return self.__id

    def get_type(self):
        return self.__type

    def set_type(self, type: str):
        self.__type = type

    def get_date(self) -> date:
        return self.__date

    def set_date(self, date: date):
        self.__date = date