from app.admin import Admin
from app.role import Role

class User:
    ''''''
    def __init__(self, user_name: str = "", password: str = "", name: str = "", id: str = ""):
        self.__id: str = id
        self.__name: str = name
        self.__user_name: str = user_name
        self.__password: str = password
        self.__role: Role

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def set_name(self, name: str):
        self.__name = name

    def get_user_name(self):
        return self.__user_name

    def set_user_name(self, user_name: str):
        self.__user_name = user_name

    def get_password(self):
        return self.__password

    def set_password(self, password: str):
        self.__password = password

    def set_role(self,role: Role):
        self.__role = role

    def get_role(self):
        return self.__role

    def is_admin(self):
        return Admin.is_admin(self)