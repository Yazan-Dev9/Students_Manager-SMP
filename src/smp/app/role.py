from enum import Enum


class Role:
    """
    Represents a role in the system with an identifier and name.

    This class encapsulates role information, allowing retrieval and modification of role ID and name.

    Attributes:
        id (int): Unique identifier for the role.
        name (str): Name of the role.

    Methods:
        get_id(): Returns the role's unique identifier.
        set_id(id: int): Sets the role's unique identifier.
        get_name(): Returns the role's name.
        set_name(name: str): Sets the role's name.
    """
    def __init__(self, name: str, id: int = 0):
        """
        Constructor for Role

        Args:
            name (str): name of role
            id (int, optional): Defaults to "".
        """
        self._id: int = id
        self._name: str = name

    def get_id(self):
        return self._id

    def set_id(self, id: int):
        self._id = id

    def get_name(self):
        return self._name

    def set_name(self, name: str):
        self._name = name


class RoleName(Enum):
    """
    An enumeration representing different user roles in the system.

    Provides predefined role names and a method to retrieve all available roles.

    Attributes:
        ADMIN (str): Represents an administrator role.
        TEACHER (str): Represents a teacher role.
        STUDENT (str): Represents a student role.
    """
    ADMIN = "admin"
    TEACHER = "teacher"
    STUDENT = "student"

    @classmethod
    def get_all_roles(cls):
        return [cls.ADMIN, cls.TEACHER, cls.STUDENT]
