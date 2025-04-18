class TeacherManager:
    ''''''
    def __init__(self):
        self.__teachers = []

    def create_teacher(self, teacher):
        self.__teachers.append(teacher)

    def get_teachers(self):
        return self.__teachers

    def get_teacher(self, id):
        for teacher in self.__teachers:
            if teacher.get_id() == id:
                return teacher
        return None

    def update_teacher(self, id, name):
        teacher = self.get_teacher(id)
        teacher.set_name(name) # type: ignore