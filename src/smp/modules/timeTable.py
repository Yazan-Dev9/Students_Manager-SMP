from classRoom import ClassRoom
from subject import Subject


class TimeTable:
    """
    Represents a time table entry with details about a specific class session.

    Attributes:
        id (int): Unique identifier for the time table entry.
        day (str): Day of the week for the class session.
        start_time (str): Start time of the class session.
        end_time (str): End time of the class session.
        subject (Subject): Subject being taught in the class session.
        class_room (ClassRoom): Classroom where the class session takes place.

    Methods provide getters and setters for accessing and modifying the time table entry's attributes.
    """
    def __init__(
        self,
        day: str,
        start_time: str,
        end_time: str,
        subject: Subject,
        class_room: ClassRoom,
        id: int = 0,
    ):
        """
        Initialize a TimeTable instance.

        Args:
            day (str): Day of the week for the class session.
            start_time (str): Start time of the class session.
            end_time (str): End time of the class session.
            subject (Subject): Subject being taught in the class session.
            class_room (ClassRoom): Classroom where the class session takes place.
            id (int, optional): Unique identifier for the time table entry. Defaults to 0.
        """
        self._id: int = id
        self._day: str = day
        self._start_time: str = start_time
        self._end_time: str = end_time
        self._subject: Subject = subject
        self._class_room: ClassRoom = class_room

    def get_id(self):
        return self._id

    def get_day(self):
        return self._day

    def set_day(self, day: str):
        self._day = day

    def get_start_time(self):
        return self._start_time

    def set_start_time(self, start_time: str):
        self._start_time = start_time

    def get_end_time(self):
        return self._end_time

    def set_end_time(self, end_time: str):
        self._end_time = end_time

    def get_subject(self) -> Subject:
        return self._subject

    def set_subject(self, subject: Subject):
        self._subject = subject

    def get_class_room(self) -> ClassRoom:
        return self._class_room

    def set_class_room(self, class_room: ClassRoom):
        self._class_room = class_room
