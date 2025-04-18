from subject import Subject

class SubjectManager:
    ''''''
    def __init__(self):
        self.__subjects = []

    def create_subject(self, subject):
        self.__subjects.append(subject)

    def get_subjects(self):
        return self.__subjects

    def get_subject(self, id):
        for subject in self.__subjects:
            if subject.get_id() == id:
                return subject
        return None

    def update_subject(self, id, name, teacher):
        subject = self.get_subject(id)
        if subject:
            subject.set_name(name)
            subject.set_teacher(teacher)

    def delete_subject(self, id):
        subject = self.get_subject(id)
        if subject:
            self.__subjects.remove(subject)

    def get_subject_by_name(self, name):
        for subject in self.__subjects:
            if subject.get_name() == name:
                return subject
        return None

    def get_subject_by_teacher(self, teacher):
        for subject in self.__subjects:
            if subject.get_teacher() == teacher:
                return subject
        return None

    def get_subject_by_student(self, student):
        for subject in self.__subjects:
            if student in subject.get_students():
                return subject
            return None