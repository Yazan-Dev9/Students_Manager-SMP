from datetime import date
from person import Person

"""
A module defining the Employee class and related enumerations for organizational roles and departments.

The Employee class extends the Person class with comprehensive employment-related attributes and methods,
providing a detailed representation of an employee's professional profile including salary, position,
employment status, and other key employment characteristics.

Includes nested classes Position and Department which serve as enumerations for standardized
organizational roles and departmental classifications.
"""


class Employee(Person):
    """
    Represents an employee with various attributes such as salary, position, and employment status.
    Inherits from the Person class and extends it with additional attributes and methods specific to employees.

    Attributes:
        salary (float): The employee's salary.
        position (str): The employee's position or job title.
        employment_status (object): The employee's employment status (e.g., "Full-time", "Part-time").
        employment_type (str): The type of employment (e.g., "Permanent", "Contract").
        employment_start_date (date): The start date of the employee's employment.
        employment_end_date (date): The end date of the employee's employment.
        employment_duration (str): The duration of the employee's employment.
        employment_department (Department): The department or division the employee belongs to (e.g., "Administration", "Education").
        employment_certificate (str): The employee's employment certificate or contract.
    """
    def __init__(self, name: str = "", id: int = 0):
        """
        Initialize an Employee instance with optional name and ID.

        Initializes employee attributes with default values, including salary,
        position, employment status, type, dates, duration, department, and certificate.

        Args:
            name (str, optional): The name of the employee. Defaults to an empty string.
            id (int, optional): The unique identifier for the employee. Defaults to 0.
        """
        super().__init__(name, id)
        self._salary: float = 0.0
        self._position: str = ""
        self._employment_status = ""
        self._employment_type = ""
        self._employment_start_date: date
        self._employment_end_date: date
        self._employment_duration: str = ""
        self._employment_department: str = ""
        self._employment_certificate: str = ""

    def set_salary(self, salary):
        self._salary = salary

    @property
    def get_salary(self):
        return self._salary

    def set_position(self, position):
        self._position = position

    @property
    def get_position(self):
        return self._position

    def set_employment_status(self, employment_status):
        self._employment_status = employment_status

    @property
    def get_employment_status(self):
        return self._employment_status

    def set_employment_type(self, employment_type):
        self._employment_type = employment_type

    @property
    def get_employment_type(self):
        return self._employment_type

    def set_employment_start_date(self, employment_start_date):
        self._employment_start_date = employment_start_date

    @property
    def get_employment_start_date(self):
        return self._employment_start_date

    def set_employment_end_date(self, employment_end_date):
        self._employment_end_date = employment_end_date

    @property
    def get_employment_end_date(self):
        return self._employment_end_date

    def set_employment_duration(self, employment_duration):
        self._employment_duration = employment_duration

    @property
    def get_employment_duration(self):
        return self._employment_duration

    def set_employment_department(self, employment_department):
        self._employment_department = employment_department

    @property
    def get_employment_department(self):
        return self._employment_department

    def set_employment_certificate(self, employment_certificate):
        self._employment_certificate = employment_certificate

    @property
    def get_employment_certificate(self):
        return self._employment_certificate


# region
# def _str_(self):
#     return f"Employee ID: {self.get_id()}, {self.get_name()}, Age: {self.get_age()} ,Salary: {self._salary}, Position: {self._position}, Employment Status: {self._employment_status}, Employment Type: {self._employment_type}, Employment Start Date: {self._employment_start_date}, Employment End Date: {self._employment_end_date}, Employment Duration: {self._employment_duration}, Employment Department: {self._employment_department}, Employment Certificate: {self._employment_certificate}"

# def calculate_salary(self):
#     return self._salary * self._working_hours

# def calculate_yearly_salary(self ):
#     return self.calculate_monthly_salary() * 12

# def calculate_weekly_salary(self):
#     return self.calculate_monthly_salary() / 4

# def calculate_monthly_salary(self, days = 30):
#     return self.calculate_salary() / days
# endregion


class Position:
    TEACHER = "Teacher"
    ADMINISTRATIVE = "Administrative"
    FACTOR = "Factor"

    @classmethod
    def get_all_positions(cls):
        return [cls.TEACHER, cls.ADMINISTRATIVE, cls.FACTOR]


class Department:
    EDUCATION = "Education"
    ADMINISTRATION = "Administration"
    MAINTENANCE = "Maintenance"
    HYGIENE = "Hygiene"
    SECURITY = "Security"
    TRANSPORTATION = "Transportation"

    @classmethod
    def get_all_positions(cls):
        return [
            cls.EDUCATION,
            cls.ADMINISTRATION,
            cls.MAINTENANCE,
            cls.HYGIENE,
            cls.SECURITY,
            cls.TRANSPORTATION,
        ]
