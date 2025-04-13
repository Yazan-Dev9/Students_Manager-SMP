import unittest
from src.smp.classRoom import ClassRoom

class TestClassRoom(unittest.TestCase):
    def setUp(self):
        self.classroom = ClassRoom("Mathematics", "101")
        
    def test_classroom_initialization(self):
        self.assertEqual(self.classroom.get_class_name(), "Mathematics")
        self.assertEqual(self.classroom.get_id(), "101")
        self.assertIsNone(self.classroom.get_class_number())
        self.assertEqual(self.classroom.get_students(), [])
        self.assertEqual(self.classroom.get_teachers(), [])
        self.assertEqual(self.classroom.get_subjects(), [])
        self.assertEqual(self.classroom.get_events(), [])
        self.assertEqual(self.classroom.get_reports(), [])
        self.assertEqual(self.classroom.get_resources(), [])

    def test_class_name_operations(self):
        self.classroom.set_class_name("Physics")
        self.assertEqual(self.classroom.get_class_name(), "Physics")

    def test_class_number_operations(self):
        self.classroom.set_class_number("Room 201")
        self.assertEqual(self.classroom.get_class_number(), "Room 201")

    def test_students_operations(self):
        test_students = ["Student1", "Student2"]
        self.classroom.set_students(test_students)
        self.assertEqual(self.classroom.get_students(), test_students)

    def test_teachers_operations(self):
        test_teachers = ["Teacher1", "Teacher2"]
        self.classroom.set_teachers(test_teachers)
        self.assertEqual(self.classroom.get_teachers(), test_teachers)

    def test_subjects_operations(self):
        test_subjects = ["Algebra", "Geometry"]
        self.classroom.set_subjects(test_subjects)
        self.assertEqual(self.classroom.get_subjects(), test_subjects)

    def test_events_operations(self):
        test_events = ["Math Quiz", "Final Exam"]
        self.classroom.set_events(test_events)
        self.assertEqual(self.classroom.get_events(), test_events)

    def test_reports_operations(self):
        test_reports = ["Progress Report", "Attendance Report"]
        self.classroom.set_reports(test_reports)
        self.assertEqual(self.classroom.get_reports(), test_reports)

    def test_resources_operations(self):
        test_resources = ["Textbook", "Calculator"]
        self.classroom.set_resources(test_resources)
        self.assertEqual(self.classroom.get_resources(), test_resources)

    def test_classroom_without_id(self):
        classroom_no_id = ClassRoom("English")
        self.assertIsNone(classroom_no_id.get_id())
        self.assertEqual(classroom_no_id.get_class_name(), "English")
