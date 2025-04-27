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
    def __init__(self, name: str = "", id : int = 0):
        self.__id: int = id
        self.__name:str  = name
        self.__mother_name: str = ""
        self.__gender: str = ""
        self.__public_number: str = "" 
        self.__date_of_birth: date
        self.__address: str = ""
        self.__phone_number: str = ""
        self.__email: str = ""
        #region
        # self.__father_name = None
        # self.__age = None
        # self.__email = None
        #endregion

    @property
    def get_id(self):
        return self.__id

    def set_id(self, id: int):
        self.__id = id

    @property
    def get_name(self):
        return self.__name

    def set_name(self, name: str):
        self.__name = name

    @property
    def get_mother_name(self):
        return self.__mother_name

    def set_mother_name(self, mother_name: str):
        self.__mother_name = mother_name

    @property
    def get_gender(self):
        return self.__gender

    def set_gender(self, gender: str):
        self.__gender = gender

    @property
    def get_date_of_birth(self) -> date:
        return self.__date_of_birth

    def set_date_of_birth(self, date_of_birth: date):
        self.__date_of_birth = date_of_birth

    @property
    def get_public_number(self):
        return self.__public_number

    def set_public_number(self, public_number: str):
        self.__public_number = public_number

    @property
    def get_address(self):
        return self.__address

    def set_address(self, address: str):
        self.__address = address

    @property
    def get_phone_number(self):
        return self.__phone_number

    def set_phone_number(self, phone_number: str):
        self.__phone_number = phone_number

    @property
    def get_email(self):
        return self.__email

    def set_email(self, email: str):
        self.__email = email

#region
    # def get_father_name(self):
    #     return self.__father_name

    # def set_father_name(self, fathe_name):
    #     self.__father_name = fathe_name

    # def get_age(self):
    #     return self.__age

    # def get_email(self):
    #     return self.__email

    # def set_email(self, email):
    #     self.__email = email

    # def __calculate_age(self, date_of_birth):
    #     today = date.today()
    #     age = today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
    #     return age

    # def __str__(self):
    #     return f"Id: {self.get_id()}, Name: {self.get_name()}, Father Name: {self.get_father_name()}, Mother Name: {self.get_mother_name()}, Age: {self.get_age()}, Gender: {self.get_gender()}, Address: {self.get_address()}, Phone Number: {self.get_phone_number()}, Email: {self.get_email()}, Date of Birth: {self.get_date_of_birth()}"
#endregion
