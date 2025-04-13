"""
A module defining the Employee class and related enumerations for organizational roles and departments.

The Employee class extends the Person class with comprehensive employment-related attributes and methods,
providing a detailed representation of an employee's professional profile including salary, position,
employment status, and other key employment characteristics.

Includes nested classes Position and Department which serve as enumerations for standardized 
organizational roles and departmental classifications.
"""
from person import Person

class Employee(Person):
    """
    Represents an employee with various attributes such as salary, position, and employment status.
    Inherits from the Person class and extends it with additional attributes and methods specific to employees.
    Attributes:
        __salary (float): The employee's salary.
        __position (Position): The employee's position or job title.
        __employment_status (object): The employee's employment status (e.g., "Full-time", "Part-time").
        __employment_type (str): The type of employment (e.g., "Permanent", "Contract"). 
        __employment_start_date (date): The start date of the employee's employment.
        __employment_end_date (date): The end date of the employee's employment.
        __employment_duration (str): The duration of the employee's employment.
        __employment_department (Department): The department or division the employee belongs to (e.g., "Administration", "Education").
        __employment_certificate (str): The employee's employment certificate or contract.
    """

    def __init__(self, name, id=None):
        super().__init__(name, id)
        self.__salary = None
        self.__position = None
        self.__employment_status = None
        self.__employment_type = None
        self.__employment_start_date = None
        self.__employment_end_date = None
        self.__employment_duration = None
        self.__employment_department = None
        self.__employment_certificate = None


    def set_salary(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_position(self, position):
        self.__position = position

    def get_position(self):
        return self.__position

    def set_employment_status(self, employment_status):
        self.__employment_status = employment_status

    def get_employment_status(self):
        return self.__employment_status

    def set_employment_type(self, employment_type):
        self.__employment_type = employment_type

    def get_employment_type(self):
        return self.__employment_type

    def set_employment_start_date(self, employment_start_date):
        self.__employment_start_date = employment_start_date

    def get_employment_start_date(self):
        return self.__employment_start_date

    def set_employment_end_date(self, employment_end_date):
        self.__employment_end_date = employment_end_date

    def get_employment_end_date(self):
        return self.__employment_end_date

    def set_employment_duration(self, employment_duration):
        self.__employment_duration = employment_duration

    def get_employment_duration(self):
        return self.__employment_duration

    def set_employment_department(self, employment_department):
        self.__employment_department = employment_department

    def get_employment_department(self):
        return self.__employment_department

    def set_employment_certificate(self, employment_certificate):
        self.__employment_certificate = employment_certificate

    def get_employment_certificate(self):
        return self.__employment_certificate

    def __str__(self):
        return f"Employee ID: {self.get_id()}, {self.get_name()}, Age: {self.get_age()} ,Salary: {self.__salary}, Position: {self.__position}, Employment Status: {self.__employment_status}, Employment Type: {self.__employment_type}, Employment Start Date: {self.__employment_start_date}, Employment End Date: {self.__employment_end_date}, Employment Duration: {self.__employment_duration}, Employment Department: {self.__employment_department}, Employment Certificate: {self.__employment_certificate}"

    # def calculate_salary(self):
    #     return self.__salary * self.__working_hours

    # def calculate_yearly_salary(self ):
    #     return self.calculate_monthly_salary() * 12

    # def calculate_weekly_salary(self):
    #     return self.calculate_monthly_salary() / 4

    # def calculate_monthly_salary(self, days = 30):
    #     return self.calculate_salary() / days

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
        return [cls.EDUCATION, cls.ADMINISTRATION, cls.MAINTENANCE, cls.HYGIENE, cls.SECURITY, cls.TRANSPORTATION]