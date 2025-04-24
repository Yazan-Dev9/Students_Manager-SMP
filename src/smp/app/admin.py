from app.role import RoleName

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

#region
    # @staticmethod
    # def infity(user_name, password):
    #     from app.managment import Managment
    #     manager = Managment()
    #     data = manager.get_user(user_name, password)
        
    #     return data
#endregion

    @staticmethod
    def is_admin(user : object):
        from app.user import User
        if (not isinstance(user, User)):
            raise TypeError("This method only accept User object")
        
        if user.get_role().get_name() == RoleName.ADMIN.value:
            return True
        else:
            return False
        
#region
        # data = __class__._infity(user.get_name(),user.get_password())
        
        # if (data):
        #     user.set_name(data[0][4])
#endregion