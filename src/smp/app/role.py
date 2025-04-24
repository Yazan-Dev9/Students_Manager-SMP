from enum import Enum

class Role:
    ''''''
    def __init__(self, name: str, id: str = ""):
        self.__id: str = id
        self.__name: str = name

    def get_id(self):
        return self.__id

    def set_id(self,id):
        self.__id = id

    def get_name(self):
        return self.__name

    def set_name(self, name: str):
        self.__name = name

class RoleName(Enum):
    ''''''
    ADMIN = "admin"
    TEACHER = "teacher"
    STUDENT = "student"

    @classmethod
    def get_all_roles(cls):
        return [cls.ADMIN, cls.TEACHER, cls.STUDENT]