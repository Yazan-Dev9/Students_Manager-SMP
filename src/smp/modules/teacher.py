# from employee import Employee
from modules.person import Person

class Teacher(Person):
    """
    A Teacher class that extends the Person class, representing an educational professional.

    Attributes:
        __courses (list): List of courses taught by the teacher.
        __classes (list): List of classrooms assigned to the teacher.
        __subjects (list): List of subjects the teacher is qualified to teach.

    Methods provide functionality to:
    - Manage courses, classes, and subjects
    """
    def __init__(self, name: str = "", id: str = ""):
        super().__init__(name,id)
        
        #region
        # super().__init__(name, id = id)
        # self.__classes = []
        # self.__subjects = []
        #endregion
#region
    # def add_class(self, classroom):
    #     self.__classes.append(classroom)

    # def get_classes(self):
    #     return self.__classes    

    # def add_subject(self, subject):
    #     self.__subjects.append(subject)

    # def get_subjects(self):
    #     return self.__subjects

    # def __str__(self):
    #     return f"Teacher ID: {self.get_id()}, Teacher: {self.get_name()}"
#endregion