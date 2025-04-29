from datetime import date
from enum import Enum

"""
A module defining Person and Gender classes for representing personal information.

The Person class allows creating and managing detailed personal records with attributes
like name, age, gender, contact details, and identification. The Gender class provides
predefined gender constants and a utility method for retrieving available genders.

Attributes:
    Person: A class representing an individual with various personal attributes.
    Gender: A utility class with gender-related constants and methods.
"""


class Person:
    """
    Represents an individual with comprehensive personal information.

    Allows creation and management of a person's details including identification,
        personal relationships, contact information, and demographic data.

    Attributes:
        name (str): The person's full name.
        id (str, optional): Unique identifier for the person.

    Methods provide getter and setter access to personal attributes such as
    name, parents, age, gender, contact details, and date of birth.
    """
    def __init__(self, name: str = "", id: int = 0):
        """
        Initialize personal attributes with provided or default values.

        Args:
            id (int, optional): Unique identifier for the person. Defaults to 0.
            name (str, optional): Full name of the person. Defaults to an empty string.

        Attributes:
            id (int): Unique identifier.
            name (str): Person's full name.
            mother_name (str): Mother's name, defaults to empty string.
            gender (str): Person's gender, defaults to empty string.
            public_number (str): Public identification number, defaults to empty string.
            date_of_birth (date): Date of birth.
            address (str): Residential address, defaults to empty string.
            phone_number (str): Contact phone number, defaults to empty string.
            email (str): Contact email address, defaults to empty string.
        """
        self._id: int = id
        self._name: str = name
        self._mother_name: str = ""
        self._gender: str = ""
        self._public_number: str = ""
        self._date_of_birth: date
        self._address: str = ""
        self._phone_number: str = ""
        self._email: str = ""
        # region
        # self._father_name = None
        # self._age = None
        # endregion

    @property
    def get_id(self):
        return self._id

    def set_id(self, id: int):
        self._id = id

    @property
    def get_name(self):
        return self._name

    def set_name(self, name: str):
        self._name = name

    @property
    def get_mother_name(self):
        return self._mother_name

    def set_mother_name(self, mother_name: str):
        self._mother_name = mother_name

    @property
    def get_gender(self):
        return self._gender

    def set_gender(self, gender: str):
        self._gender = gender

    @property
    def get_date_of_birth(self) -> date:
        return self._date_of_birth

    def set_date_of_birth(self, date_of_birth: date):
        self._date_of_birth = date_of_birth

    @property
    def get_public_number(self):
        return self._public_number

    def set_public_number(self, public_number: str):
        self._public_number = public_number

    @property
    def get_address(self):
        return self._address

    def set_address(self, address: str):
        self._address = address

    @property
    def get_phone_number(self):
        return self._phone_number

    def set_phone_number(self, phone_number: str):
        self._phone_number = phone_number

    @property
    def get_email(self):
        return self._email

    def set_email(self, email: str):
        self._email = email


# region
# def get_father_name(self):
#     return self._father_name

# def set_father_name(self, father_name):
#     self._father_name = father_name

# def get_age(self):
#     return self._age

# def get_email(self):
#     return self._email

# def set_email(self, email):
#     self._email = email

# def _calculate_age(self, date_of_birth):
#     today = date.today()
#     age = today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
#     return age

# def _str_(self):
#     return f"Id: {self.get_id()}, Name: {self.get_name()}, Father Name: {self.get_father_name()}, Mother Name: {self.get_mother_name()}, Age: {self.get_age()}, Gender: {self.get_gender()}, Address: {self.get_address()}, Phone Number: {self.get_phone_number()}, Email: {self.get_email()}, Date of Birth: {self.get_date_of_birth()}"
# endregion


class Gender(Enum):
    """
    Provides an enumeration of gender types and utility methods for gender-related operations.

    This class defines standard gender constants and offers a method to retrieve all available genders.
    Supports basic gender representation with MALE and FEMALE options.

    Attributes:
        MALE (str): Represents the male gender.
        FEMALE (str): Represents the female gender.
    """

    MALE = "male"
    FEMALE = "female"

    @classmethod
    def get_all_genders(cls):
        return [cls.MALE, cls.FEMALE]
