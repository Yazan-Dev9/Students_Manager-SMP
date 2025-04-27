from modules.teacher import Teacher
from modules.classRoom import ClassRoom

class Subject:
    ''''''
    def __init__(self, subject_name: str = "", subject_id: int = 0):
        self._id: int = subject_id
        self._name: str = subject_name
        self._teacher: Teacher
        self._class_room : ClassRoom
        self._description: str = ""
        #region
        # self._teacher = teacher
        # self._students = []
        # self._attendance_hours = 0
        # self._resources = []
        #endregion

    @property
    def get_id(self):
        return self._id

    def set_id(self, id: int):
        self._id = id

    def set_name(self, name: str):
        self._name = name

    @property
    def get_name(self):
        return self._name

    def set_teacher(self, teacher: Teacher):
        self._teacher = teacher

    @property
    def get_teacher(self):
        return self._teacher

    @property
    def get_description(self):
        return self._description

    def set_description(self, description: str):
        self._description = description

    @property
    def get_class(self):
        return self._class_room

    def set_class(self,class_room):
        self._class_room = class_room

#region
    # def set_teacher(self, teacher):
    #     self._teacher = teacher

    # def get_teacher(self):
    #     return self._teacher

    # def add_student(self, student):
    #     self._students.append(student)

    # def get_students(self):
    #     return self._students

    # def set_attendance_hours(self, hours):
    #     self._attendance_hours = hours

    # def get_attendance_hours(self):
    #     return self._attendance_hours

    # def set_resources(self, resource):
    #     self._resources.append(resource)

    # def get_resources(self):
    #     return self._resources

    # def _str_(self):
    #     return f"Subject ID: {self._id}, Name: {self._name} - Teacher: {self._teacher}"
#endregion
