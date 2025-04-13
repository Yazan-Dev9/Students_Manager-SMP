class ClassManager:
    """
    A class for managing students, classes, and classroom-related operations.
    
    Attributes:
        __classRooms (list): A private list storing classroom objects.
    
    Methods:
        create_class(classRoom): Adds a new classroom to the list of classrooms.
        remove_class(): Placeholder method for removing a class (not implemented).
        add_student_to_class(student, classRoom): Adds a student to a classroom .
        add_teacher_to_class(teacher, classRoom): Placeholder method for adding a teacher to a classroom (not implemented).
        drup_student(name): Placeholder method for dropping a student (not implemented).
    """
    def __init__(self):
        self.__classRooms = []

    def create_class(self, class_room):
        self.__classRooms.append(class_room)

    def remove_class(self):
        pass

    def add_student_to_class(self, student, class_room):
        student.add_t

    def add_teacher_to_class(self, teacher, class_room):
        teacher.get_classes().append(class_room)

    def drup_student(self, name):
        pass

    def drup_teacher(self, name):
        pass