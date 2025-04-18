class Subject:
    ''''''
    def __init__(self, name, teacher, id = None):
        self.__id = id
        self.__name = name
        self.__teacher = teacher
        self.__students = []
        self.__attendance_hours = 0
        self.__total_grades = 0
        self.__resources = []

    def get_id(self):
        return self.__id

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_teacher(self, teacher):
        self.__teacher = teacher

    def get_teacher(self):
        return self.__teacher

    def add_student(self, student):
        self.__students.append(student)

    def get_students(self):
        return self.__students

    def set_attendance_hours(self, hours):
        self.__attendance_hours = hours

    def get_attendance_hours(self):
        return self.__attendance_hours

    def set_total_grades(self, grades):
        self.__total_grades = grades

    def get_total_grades(self):
        return self.__total_grades

    def set_resources(self, resource):
        self.__resources.append(resource)

    def get_resources(self):
        return self.__resources

    def __str__(self):
        return f"Subject ID: {self.__id}, Name: {self.__name} - Teacher: {self.__teacher}"