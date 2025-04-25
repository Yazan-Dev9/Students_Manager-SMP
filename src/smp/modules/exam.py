from datetime import date
from enum import Enum
from modules.subject import Subject

class ExamType(Enum):
    ''''''
    MIDTERM = "midterm"
    FINAL = "final"
    QUIZ = "quiz"
    @classmethod
    def get_all_types(cls):
        return [cls.MIDTERM, cls.FINAL, cls.QUIZ]

class Exam:
    ''''''
    def __init__(self, type: str = "", id: str = "" ):
        self.__id: str = id
        self.__type: str = type
        self.__date: date
        self.__description = ""
        self.__subject: Subject

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

    def get_description(self):
        return self.__description

    def set_description(self, description: str):
        self.__description = description

    def get_subject(self) -> Subject:
        return self.__subject

    def set_subject(self, subject: Subject):
        self.__subject = subject
