from modules.person import Person
from modules.classRoom import ClassRoom


class Student(Person):
    """
    Represents a student in the school management system, inheriting from the Person class.

    Attributes:
        grade (str): The grade level of the student.
        class_room (ClassRoom): The classroom assigned to the student.

    Methods:
        get_grade: Property to retrieve the student's grade.
        set_grade: Method to set the student's grade.
        get_class: Property to retrieve the student's classroom.
        set_class: Method to assign a classroom to the student.
    """
    def __init__(self, name: str = "", id: int = 0):
        """"""
        super().__init__(name, id)
        self._grade: str = ""
        self._class_room: ClassRoom
        # region
        # self.__classes = None
        # self.__average = 0.0
        # self.__attendance_hours = 0
        # endregion

    @property
    def get_grade(self):
        return self._grade

    def set_grade(self, grade: str):
        self._grade = grade

    @property
    def get_class(self):
        return self._class_room

    def set_class(self, class_room: ClassRoom):
        self._class_room = class_room

    # region
    # def add_grade(self, grade):
    #     self.__grades.append(grade)
    #     # self.__calculate_average()

    # def get_grades(self):
    #     return self.__grades

    # def get_classes(self):
    #     return self.__classes

    # def add_to_class(self, classes):
    #     self.__classes.append(classes)

    # def get_average(self):
    #     return self.__average

    # def set_attendance_hours(self, hours):
    #     self.__attendance_hours = hours

    # def get_attendance_hours(self):
    #     return self.__attendance_hours

    # def __calculate_average(self):
    #     if len(self.__grades) > 0:
    #         self.__average = sum(self.__grades) / len(self.__grades)
    #     else:
    #         self.__average = 0.0

    # def __str__(self):
    #     return f"Student ID: {self.get_id()}, Student: {self.get_name()}, Average: {self.get_average()}"
    # endregion
