"""
"""
from app.role import RoleName


class Admin:
    """
    Represents an administrative user in the system.

    This class manages admin-specific attributes and provides methods for checking administrative privileges.

    Attributes:
        id (int): Unique identifier for the admin.
        name (str): Name of the admin.

    Methods:
        get_id: Property to retrieve the admin's ID.
        get_name: Property to retrieve the admin's name.
        set_name: Allows updating the admin's name.
        is_admin: Static method to check if a user has admin role.
    """
    def __init__(self, name: str, id: int = 0):
        """
        Constructor for Admin

        Args:
            name (str): name of admin
            id (int, optional): ID Defaults to 0.
        """
        self._id: int = id
        self._name: str = name

    @property
    def get_id(self):
        return self._id

    @property
    def get_name(self):
        return self._name

    def set_name(self, name: str):
        self._name = name

    @staticmethod
    def is_admin(user: object):
        """
        Check if user is admin

        Args:
            user (User): User object

        Raises:
            TypeError: His method only accept User object

        Returns:
            Boolean: True if user is admin, False otherwise
        """
        from app.user import User

        if not isinstance(user, User):
            raise TypeError("This method only accept User object")

        if user.get_role().get_name() == RoleName.ADMIN.value:
            return True
        else:
            return False
