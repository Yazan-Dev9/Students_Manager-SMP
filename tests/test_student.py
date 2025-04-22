import unittest
from datetime import date
from smp.module.student import Student

class TestStudent(unittest.TestCase):
    def setUp(self):
        self.student = Student("Jane Smith", "456")

    def test_student_initialization(self):
        self.assertEqual(self.student.get_name(), "Jane Smith")
        self.assertEqual(self.student.get_id(), "456")
        self.assertEqual(self.student.get_grades(), [])
        self.assertEqual(self.student.get_classes(), [])
        self.assertEqual(self.student.get_average(), 0.0)

    def test_add_single_grade(self):
        self.student.add_grade(85)
        self.assertEqual(self.student.get_grades(), [85])
        self.assertEqual(self.student.get_average(), 85.0)

    def test_add_multiple_grades(self):
        grades = [85, 90, 95]
        for grade in grades:
            self.student.add_grade(grade)
        self.assertEqual(self.student.get_grades(), grades)
        self.assertEqual(self.student.get_average(), 90.0)

    def test_empty_grades_average(self):
        self.assertEqual(self.student.get_average(), 0.0)

    def test_set_and_get_classes(self):
        classes = ["Math", "Science", "History"]
        self.student.set_classes(classes)
        self.assertEqual(self.student.get_classes(), classes)

    def test_grade_precision(self):
        self.student.add_grade(85.5)
        self.student.add_grade(90.5)
        self.assertEqual(self.student.get_average(), 88.0)

    def test_inherited_person_attributes(self):
        self.student.set_father_name("John Smith")
        self.student.set_mother_name("Mary Smith")
        birth_date = date(2000, 1, 1)
        self.student.set_date_of_birth(birth_date)
        
        self.assertEqual(self.student.get_father_name(), "John Smith")
        self.assertEqual(self.student.get_mother_name(), "Mary Smith")
        self.assertEqual(self.student.get_date_of_birth(), birth_date)
