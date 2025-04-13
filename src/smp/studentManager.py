class StudentManager:
    """
    A class for managing a collection of students with various search and retrieval methods.
    
    Provides functionality to:
    - Add students to the collection
    - Retrieve students by different criteria (name, class, age, average)
    - Maintain a private list of students
    
    Attributes:
        __students (list): A private list storing Student objects
    """
    def __init__(self):
        self.__students = []

    def add_student(self, student):
        self.__students.append(student)

    def get_students(self):
        return self.__students

    def get_student_by_name(self, name):
        for student in self.__students:
            if student.get_name() == name:
                return student
        return None

    def get_students_by_class(self, class_name):
        students = []
        for student in self.__students:
            if student.get_classes().get_class_name() == class_name:
                students.append(student)
        return students

    def get_students_by_age(self, age):
        students = []
        for student in self.__students:
            if student.get_age() == age:
                students.append(student)
        return students

    def get_students_by_average(self, average):
        students = []
        for student in self.__students:
            if student.get_average() == average:
                students.append(student)
        return students

    def delete_student(self,name):
        pass