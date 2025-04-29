class ClassRoom:
    """
    A class representing a classroom with attributes such as identifier, name, capacity, and division.

    This class provides methods to get and set various properties of a classroom,
    including its unique ID, name, student capacity, and division number.

    Attributes:
        id (int): Unique identifier for the classroom.
        name (str): Name of the classroom.
        division (int): Division number of the classroom.
        capacity (int): Maximum number of students the classroom can accommodate.
        grade (str): Grade level associated with the classroom (currently commented out).

    Methods:
        get_id: Property to retrieve the classroom's unique identifier.
        set_id: Method to set the classroom's unique identifier.
        get_name: Property to retrieve the classroom's name.
        set_name: Method to set the classroom's name.
        get_capacity: Property to retrieve the classroom's student capacity.
        set_capacity: Method to set the classroom's student capacity with validation.
        get_division: Property to retrieve the classroom's division number.
        set_division: Method to set the classroom's division number with validation.
    """
    def __init__(self, name: str = "", id: int = 0) -> None:
        """
        Initializes a new ClassRoom instance.

        Args:
            name (str): The name of the classroom.
            id (int): The unique identifier for the classroom.
        """
        self._id: int = id
        self._name: str = name
        self._division: int = 0
        self._capacity: int = 0
        self._grade: str = ""

    @property
    def get_id(self) -> int:
        """
        Returns the unique identifier of the classroom.

        :return: Class ID as a integer
        """
        return self._id

    def set_id(self, id: int):
        """
        Sets the ID of the classroom.
        """
        self._id = id

    @property
    def get_name(self) -> str:
        """
        Returns the name of the classroom.

        :return: Class name as a string
        """

        return self._name

    def set_name(self, new_name: str):
        """
        Sets the name of the classroom.
        """
        self._name = new_name

    # @property
    # def get_grade(self) -> str:
    #     """
    #     Returns the grade level associated with the classroom.

    #     :return: Grade level as a string
    #     """
    #     return self._grade

    # def set_grade(self, value: str):
    #     """Sets the grade level for the classroom."""
    #     self._grade = value

    @property
    def get_capacity(self) -> int:
        """
        Returns the capacity of the classroom (number of students it can hold).

        :return: Capacity number as a integer
        """
        return self._capacity

    def set_capacity(self, value: int):
        """
        Sets the capacity of the classroom.
        """
        if value <= 0:
            raise ValueError("Capacity cannot be negative.")
        self._capacity = value

    @property
    def get_division(self) -> int:
        """
        Returns the division of the classroom (number of class room).

        :return: Division number as a integer
        """
        return self._division

    def set_division(self, value: int):
        """
        Sets the division of the classroom.
        """
        if value < 0:
            raise ValueError("Division cannot be negative.")
        self._division = value
