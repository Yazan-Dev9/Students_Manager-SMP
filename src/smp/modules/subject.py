from teacher import Teacher

class Subject:
    ''''''
    def __init__(self, name, teacher: Teacher, id: str = ""):
        self.__id: str = id
        self.__name = name
        self.__teacher = teacher
        #region
        # self.__teacher = teacher
        # self.__students = []
        # self.__attendance_hours = 0
        # self.__resources = []
        #endregion

    def get_id(self):
        return self.__id

    def set_name(self, name: str):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_teacher(self, teacher: Teacher):
        self.__teacher = teacher

    def get_teacher(self):
        return self.__teacher

#region
    # def set_teacher(self, teacher):
    #     self.__teacher = teacher

    # def get_teacher(self):
    #     return self.__teacher

    # def add_student(self, student):
    #     self.__students.append(student)

    # def get_students(self):
    #     return self.__students

    # def set_attendance_hours(self, hours):
    #     self.__attendance_hours = hours

    # def get_attendance_hours(self):
    #     return self.__attendance_hours

    # def set_resources(self, resource):
    #     self.__resources.append(resource)

    # def get_resources(self):
    #     return self.__resources

    # def __str__(self):
    #     return f"Subject ID: {self.__id}, Name: {self.__name} - Teacher: {self.__teacher}"
#endregion
