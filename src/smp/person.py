from datetime import date
"""
A module defining Person and Gender classes for representing personal information.

The Person class allows creating and managing detailed personal records with attributes
like name, age, gender, contact details, and identification. The Gender class provides
predefined gender constants and a utility method for retrieving available genders.

Attributes:
    Person: A class representing an individual with various personal attributes.
    Gender: A utility class with gender-related constants and methods.
"""

class Person(object):
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
    def __init__(self, name, id = None):
        self.__id = id
        self.__name = name
        self.__father_name = None
        self.__mother_name = None
        self.__gender = None
        self.__person_number = None 
        self.__date_of_birth = None
        self.__age = None
        self.__address = None
        self.__phone_number = None
        self.__email = None

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_father_name(self):
        return self.__father_name

    def set_father_name(self, fathe_name):
        self.__father_name = fathe_name

    def get_mother_name(self):
        return self.__mother_name

    def set_mother_name(self, mother_name):
        self.__mother_name = mother_name

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        self.__gender = gender

    def get_date_of_birth(self):
        return self.__date_of_birth

    def set_date_of_birth(self, date_of_birth):
        self.__age = self.__calculate_age(date_of_birth)
        self.__date_of_birth = date_of_birth

    def get_age(self):
        return self.__age

    def get_person_number(self):
        return self.__person_number

    def set_person_number(self, person_number):
        self.__person_number = person_number

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address

    def get_phone_number(self):
        return self.__phone_number

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def __calculate_age(self, date_of_birth):
        today = date.today()
        age = today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
        return age

    def __str__(self):
        return f"Id: {self.get_id()}, Name: {self.get_name()}, Father Name: {self.get_father_name()}, Mother Name: {self.get_mother_name()}, Age: {self.get_age()}, Gender: {self.get_gender()}, Address: {self.get_address()}, Phone Number: {self.get_phone_number()}, Email: {self.get_email()}, Date of Birth: {self.get_date_of_birth()}"


class Gender:
    """
    Provides an enumeration of gender types and utility methods for gender-related operations.
    
    This class defines standard gender constants and offers a method to retrieve all available genders.
    Supports basic gender representation with MALE and FEMALE options.
    
    Attributes:
        MALE (str): Represents the male gender.
        FEMALE (str): Represents the female gender.
    """
    MALE = "Male"
    FEMALE = "Female"

    @classmethod
    def get_all_genders(cls):
        return [cls.MALE, cls.FEMALE]
