# from employee import Employee
from modules.person import Person


class Teacher(Person):
    """
    Represents a Teacher in the school management system, inheriting from Person.

    Attributes:
        name (str): The name of the teacher, defaults to an empty string.
        id (int): The unique identifier for the teacher, defaults to 0.

    Initializes a Teacher object with optional name and ID, setting up base Person attributes.
    """
    def __init__(self, name: str = "", id: int = 0):
        """
        Initialize a Teacher object.

        Args:
            name (str, optional): The name of the teacher. Defaults to an empty string.
            id (int, optional): The unique identifier for the teacher. Defaults to 0.

        Calls the parent class (Person) constructor to set up base attributes.
        """
        super().__init__(name, id)

        # region
        # self.__classes = []
        # self.__subjects = []
        # endregion


# region
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
# endregion
