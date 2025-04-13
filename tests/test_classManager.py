import unittest
from src.smp.teacher import Teacher
from src.smp.classManager import ClassManager
from src.smp.classRoom import ClassRoom
from src.smp.student import Student


class TestClassManagerMore(unittest.TestCase):
    def setUp(self):
        self.class_manager = ClassManager()
        self.classroom1 = ClassRoom("Mathematics", "101")
        self.classroom2 = ClassRoom("Physics", "102")
        self.student1 = Student("yazan", "123")
        self.student2 = Student("ahmad", "456")


    def test_add_student_to_multiple_classes(self):
        self.class_manager.create_class(self.classroom1)
        self.class_manager.create_class(self.classroom2)
        self.class_manager.add_student_to_class(self.student1, self.classroom1)
        self.class_manager.add_student_to_class(self.student1, self.classroom2)
        self.assertIn(self.classroom1, self.student1.get_classes())
        self.assertIn(self.classroom2, self.student1.get_classes())

    def test_add_multiple_students_to_class(self):
        self.class_manager.create_class(self.classroom1)
        self.class_manager.add_student_to_class(self.student1, self.classroom1)
        self.class_manager.add_student_to_class(self.student2, self.classroom1)
        self.assertIn(self.classroom1, self.student1.get_classes())
        self.assertIn(self.classroom1, self.student2.get_classes())

    def test_create_multiple_classes(self):
        self.class_manager.create_class(self.classroom1)
        self.class_manager.create_class(self.classroom2)
        self.assertIn(self.classroom1, self.class_manager._ClassManager__classRooms) # type: ignore
        self.assertIn(self.classroom2, self.class_manager._ClassManager__classRooms) # type: ignore

    def test_add_teacher_to_class(self):
        teacher = Teacher("Teacher", "789")  # Using Student as Teacher for simplicity
        self.class_manager.create_class(self.classroom1)
        self.class_manager.add_teacher_to_class(teacher, self.classroom1)
        self.assertIn(self.classroom1, teacher.get_classes())
