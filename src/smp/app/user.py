from app.admin import Admin
from app.role import Role


class User:
    """
    Represents a user in the system with attributes and methods for managing user information.

    Attributes:
        id (int): Unique identifier for the user.
        name (str): Full name of the user.
        user_name (str): Username for authentication.
        password (str): User's password.
        role (Role): Role assigned to the user.

    Methods provide getters and setters for user attributes, as well as role management and admin status checking.
    """

    def __init__(
        self, user_name: str = "", password: str = "", name: str = "", id: int = 0
    ):
        """
        Constructor for User

        Args:
            user_name (str, optional): Defaults to "".
            password (str, optional): Defaults to "".
            name (str, optional): Defaults to "".
            id (int, optional): Defaults to "".
        """
        self._id: int = id
        self._name: str = name
        self._user_name: str = user_name
        self._password: str = password
        self._role: Role

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def set_name(self, name: str):
        self._name = name

    def get_user_name(self):
        return self._user_name

    def set_user_name(self, user_name: str):
        self._user_name = user_name

    def get_password(self):
        return self._password

    def set_password(self, password: str):
        self._password = password

    def set_role(self, role: Role):
        self._role = role

    def get_role(self):
        return self._role

    def is_admin(self):
        return Admin.is_admin(self)
