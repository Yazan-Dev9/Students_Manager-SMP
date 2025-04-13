class ClassRoom:
    """
    A class representing a classroom with various attributes and methods for managing its details.
    
    Attributes:
        __id (int, optional): Unique identifier for the classroom.
        __class_name (str): Name of the classroom.
        __class_number (str, optional): Number or identifier of the classroom.
        __students (list): List of students in the classroom.
        __teachers (list): List of teachers associated with the classroom.
        __subjects (list): List of subjects taught in the classroom.
        __events (list): List of events related to the classroom.
        __reports (list): List of reports associated with the classroom.
        __resources (list): List of resources available in the classroom.
    
    Methods provide getters and setters for all attributes, allowing manipulation of classroom details.
    """
    def __init__(self, class_name, id = None):
        self.__id = id
        self.__class_name = class_name
        self.__class_number = None
        self.__students = []
        self.__teachers = []
        self.__subjects = []
        self.__events = []
        self.__reports = []
        self.__resources = []

    def get_id(self):
        return self.__id

    def get_class_name(self):
        return self.__class_name

    def set_class_name(self, class_name):
        self.__class_name = class_name

    def get_class_number(self):
        return self.__class_number

    def set_class_number(self, class_number):
        self.__class_number = class_number

    def get_students(self):
        return self.__students

    def set_students(self, students):
        self.__students = students

    def get_teachers(self):
        return self.__teachers

    def set_teachers(self, teachers):
        self.__teachers = teachers

    def get_subjects(self):
        return self.__subjects

    def set_subjects(self, subjects):
        self.__subjects = subjects

    def get_events(self):
        return self.__events

    def set_events(self, events):
        self.__events = events

    def get_resources(self):
        return self.__resources

    def set_reports(self, reports):
        self.__reports = reports

    def get_reports(self):
            return self.__reports

    def set_resources(self, resources):
        self.__resources = resources

    def __str__(self):
        return f"Class Room ID: {self.__id}, Class Name: {self.__class_name}, Class Number: {self.__class_number}"