from exam import Exam
from student import Student


class Grade:
    """
    Represents a grade associated with a student and an exam.

    Attributes:
        id (int): Unique identifier for the grade.
        exam (Exam): The exam associated with this grade.
        score (float): The numerical score achieved for the exam.
        student (Student): The student who received this grade.

    Properties and methods allow getting and setting the grade's attributes.
    """
    def __init__(self, score: float = 0.0, id: int = 0):
        """
        Initialize the grade's attributes.

        Args:
            score (float, optional): The numerical score achieved for the exam. Defaults to 0.0.
            id (int, optional): Unique identifier for the grade. Defaults to 0.
        """
        self._id: int = id
        self._exam: Exam
        self._score: float = score
        self._student: Student

    @property
    def get_id(self):
        return self._id

    @property
    def get_exam(self) -> Exam:
        return self._exam

    def set_exam(self, exam: Exam):
        self._exam = exam

    @property
    def get_score(self):
        return self._score

    def set_score(self, score: float):
        self._score = score

    @property
    def get_student(self) -> Student:
        return self._student

    def set_student(self, student: Student):
        self._student = student
