from datetime import date
from enum import Enum
from modules.student import Student


class Attendance:
    """
    Represents an attendance record for a student.

    Tracks the attendance status, date, and associated student information.
    Provides methods to get and set attendance details.

    Attributes:
        id (int): Unique identifier for the attendance record.
        status (str): Attendance status (e.g., Present, Absent, Late).
        date (date): Date of the attendance record.
        student (Student): Student associated with the attendance record.
    """
    def __init__(self, status: str = "", id: int = 0):
        """
        Constructor  for Attendance

        Args:
            status (str, optional): Defaults to "".
            id (int, optional): Defaults to 0.
        """
        self._id: int = id
        self._status: str = status
        self._date: date
        self._student: Student

    @property
    def get_id(self):
        return self._id

    @property
    def get_status(self):
        return self._status

    def set_status(self, status: str):
        self._status = status

    @property
    def get_date(self) -> date:
        return self._date

    def set_date(self, date: date):
        self._date = date

    @property
    def get_student(self) -> Student:
        return self._student

    def set_student(self, student: Student):
        self._student = student


class Status(Enum):
    """
    Enumeration representing possible attendance statuses.

    Provides predefined status values for tracking student attendance.

    Attributes:
        PRESENT (str): Indicates the student was present.
        ABSENT (str): Indicates the student was absent.
        LATE (str): Indicates the student arrived late.

    Methods:
        get_all_status(): Returns a list of all available attendance statuses.
    """

    PRESENT = "Present"
    ABSENT = "Absent"
    LATE = "Late"

    @classmethod
    def get_all_status(cls):
        return [cls.PRESENT, cls.ABSENT, cls.LATE]
