from datetime import date
from enum import Enum
from modules.subject import Subject
from modules.classRoom import ClassRoom


class ExamType(Enum):
    """
    Enumeration representing types of exams.
    """

    MIDTERM = "midterm"
    FINAL = "final"
    QUIZ = "quiz"

    @classmethod
    def get_all_types(cls):
        """
        Returns a list of all possible exam types.

        :return: List of ExamType members
        """
        return [cls.MIDTERM, cls.FINAL, cls.QUIZ]


class Exam:
    """
    Represents an exam with attributes like id, type, date, description, and subject.
    Provides getter and setter methods to access and modify these attributes.
    """

    def __init__(self, exam_type: str = "", exam_id: str = ""):
        """
        Initializes an Exam instance.

        Args:
            exam_type (ExamType as str) : The type of the exam (e.g., 'midterm', 'final', 'quiz')
            exam_id (str) : Unique identifier for the exam
        """
        self._id: str = exam_id
        self._type: str = exam_type
        self._date: date
        self._description = ""
        self._subject: Subject
        self._class: ClassRoom

    @property
    def get_id(self) -> str:
        """
        Returns the unique identifier of the exam.

        :return: Exam ID as a string
        """
        return self._id

    @property
    def get_type(self) -> str:
        """
        Returns the type of the exam.

        :return: Exam type as a string
        """
        return self._type

    def set_type(self, type: str):
        """
        Sets the type of the exam.

        :param type: New exam type as a string by Class ExamType
        """
        self._type = type

    @property
    def get_date(self) -> date:
        """
        Returns the date on which the exam is scheduled.

        :return: Exam date as a datetime.date object
        """
        return self._date

    def set_date(self, date: date):
        """
        Sets the date for the exam.

        :param date: Exam date as a datetime.date object
        """
        self._date = date

    @property
    def get_description(self) -> str:
        """
        Returns the description of the exam.

        :return: Exam description as a string
        """
        return self._description

    def set_description(self, description: str):
        """
        Sets the description for the exam.

        :param description: Description text as a string
        """
        self._description = description

    @property
    def get_subject(self) -> Subject:
        """
        Returns the subject associated with the exam.

        :return: Subject instance
        """
        return self._subject

    def set_subject(self, subject: Subject):
        """
        Sets the subject for the exam.

        :param subject: Subject instance
        """
        self._subject = subject

    @property
    def get_class(self) -> ClassRoom:
        """
        Returns the class associated with the exam.

        :return: ClssRoom instance
        """
        return self._class

    def set_class(self, class_room: ClassRoom):
        """
        Sets the class for the exam.

        :param class_room: ClassRoom instance
        """
        self._class = class_room
