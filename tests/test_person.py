import unittest
from datetime import date
from src.smp.person import Person, Gender

class TestPerson(unittest.TestCase):
    def setUp(self):
        self.person = Person("John Doe", "123")

    def test_person_initialization(self):
        self.assertEqual(self.person.get_name(), "John Doe")
        self.assertEqual(self.person.get_id(), "123")
        self.assertIsNone(self.person.get_father_name())
        self.assertIsNone(self.person.get_mother_name())
        self.assertIsNone(self.person.get_age())
        self.assertIsNone(self.person.get_gender())
        self.assertIsNone(self.person.get_address())
        self.assertIsNone(self.person.get_phone_number())
        self.assertIsNone(self.person.get_email())
        self.assertIsNone(self.person.get_date_of_birth())

    def test_person_setters(self):
        self.person.set_name("Jane Doe")
        self.person.set_father_name("John Sr")
        self.person.set_mother_name("Mary")
        self.person.set_gender(Gender.FEMALE)
        self.person.set_address("123 Main St")
        self.person.set_phone_number("555-1234")
        self.person.set_email("jane@example.com")
        
        self.assertEqual(self.person.get_name(), "Jane Doe")
        self.assertEqual(self.person.get_father_name(), "John Sr")
        self.assertEqual(self.person.get_mother_name(), "Mary")
        self.assertEqual(self.person.get_gender(), Gender.FEMALE)
        self.assertEqual(self.person.get_address(), "123 Main St")
        self.assertEqual(self.person.get_phone_number(), "555-1234")
        self.assertEqual(self.person.get_email(), "jane@example.com")

    def test_date_of_birth_and_age_calculation(self):
        birth_date = date(1990, 6, 15)
        self.person.set_date_of_birth(birth_date)
        
        today = date.today()
        expected_age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        
        self.assertEqual(self.person.get_date_of_birth(), birth_date)
        self.assertEqual(self.person.get_age(), expected_age)

    def test_str_representation(self):
        self.person.set_father_name("John Sr")
        self.person.set_mother_name("Mary")
        self.person.set_gender(Gender.MALE)
        self.person.set_address("123 Main St")
        self.person.set_phone_number("555-1234")
        self.person.set_email("john@example.com")
        birth_date = date(1990, 6, 15)
        self.person.set_date_of_birth(birth_date)
        
        expected_str = f"Id: 123, Name: John Doe, Father Name: John Sr, Mother Name: Mary, Age: {self.person.get_age()}, Gender: Male, Address: 123 Main St, Phone Number: 555-1234, Email: john@example.com, Date of Birth: {birth_date}"
        self.assertEqual(str(self.person), expected_str)

class TestGender(unittest.TestCase):
    def test_gender_constants(self):
        self.assertEqual(Gender.MALE, "Male")
        self.assertEqual(Gender.FEMALE, "Female")

    def test_get_all_genders(self):
        genders = Gender.get_all_genders()
        self.assertEqual(len(genders), 2)
        self.assertIn(Gender.MALE, genders)
        self.assertIn(Gender.FEMALE, genders)
        self.assertEqual(genders, ["Male", "Female"])
