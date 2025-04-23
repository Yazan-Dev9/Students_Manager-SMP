class Admin:
    ''''''
    def __init__(self, name: str, id: str = ""):
        self.__id: str = id
        self.__name: str = name

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def set_name(self, name: str):
        self.__name = name

    @staticmethod
    def is_admin(user : object):
        # TODO check if user in admin table
        from app.user import User
        if (not isinstance(user, User)):
            raise TypeError("This method only accept User object")
        
        if (user.get_user_name() == "admin" and user.get_password() == "123"):
            user.set_name("Yk")
            return True
        else:
            return False
