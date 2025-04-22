import unittest
from datetime import date
from smp.module.student import Student
from src.smp.studentManager import StudentManager
from smp.module.classRoomoom import ClassRoom

class TestStudentManager(unittest.TestCase):
    def setUp(self):
        self.manager = StudentManager()
        self.student1 = Student("John Doe", "123")
        self.student2 = Student("Jane Smith", "456")
        self.student3 = Student("Bob Wilson", "789")
        
        # Setup student1
        self.student1.add_grade(85)
        self.student1.add_grade(90)
        self.student1.set_date_of_birth(date(2000, 1, 1))
        math_class = ClassRoom("Math", "101")
        self.student1.set_classes([math_class])
        
        # Setup student2
        self.student2.add_grade(95)
        self.student2.set_date_of_birth(date(2001, 6, 15))
        science_class = ClassRoom("Science", "102")
        self.student2.set_classes([science_class])
        
        # Setup student3
        self.student3.add_grade(85)
        self.student3.set_date_of_birth(date(2000, 1, 1))
        self.student3.set_classes([math_class])

    def test_add_and_get_students(self):
        self.manager.add_student(self.student1)
        self.manager.add_student(self.student2)
        self.assertEqual(len(self.manager.get_students()), 2)
        self.assertIn(self.student1, self.manager.get_students())
        self.assertIn(self.student2, self.manager.get_students())

    def test_get_student_by_name(self):
        self.manager.add_student(self.student1)
        self.manager.add_student(self.student2)
        found_student = self.manager.get_student_by_name("John Doe")
        self.assertEqual(found_student, self.student1)
        self.assertIsNone(self.manager.get_student_by_name("Nonexistent Student"))

    def test_get_students_by_class(self):
        self.manager.add_student(self.student1)
        self.manager.add_student(self.student2)
        self.manager.add_student(self.student3)
        math_students = self.manager.get_students_by_class("Math")
        self.assertEqual(len(math_students), 2)
        self.assertIn(self.student1, math_students)
        self.assertIn(self.student3, math_students)
        
        science_students = self.manager.get_students_by_class("Science")
        self.assertEqual(len(science_students), 1)
        self.assertIn(self.student2, science_students)

    def test_get_students_by_age(self):
        self.manager.add_student(self.student1)
        self.manager.add_student(self.student2)
        self.manager.add_student(self.student3)
        
        today = date.today()
        age1 = today.year - 2000 - ((today.month, today.day) < (1, 1))
        students_age1 = self.manager.get_students_by_age(age1)
        self.assertEqual(len(students_age1), 2)
        self.assertIn(self.student1, students_age1)
        self.assertIn(self.student3, students_age1)

    def test_get_students_by_average(self):
        self.manager.add_student(self.student1)
        self.manager.add_student(self.student2)
        self.manager.add_student(self.student3)
        
        students_85 = self.manager.get_students_by_average(85.0)
        self.assertEqual(len(students_85), 1)
        self.assertIn(self.student3, students_85)
        
        students_87_5 = self.manager.get_students_by_average(87.5)
        self.assertEqual(len(students_87_5), 1)
        self.assertIn(self.student1, students_87_5)

    def test_empty_manager(self):
        self.assertEqual(len(self.manager.get_students()), 0)
        self.assertEqual(self.manager.get_students_by_class("Math"), [])
        self.assertEqual(self.manager.get_students_by_age(20), [])
        self.assertEqual(self.manager.get_students_by_average(85.0), [])
