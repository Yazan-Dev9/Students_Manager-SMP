from classRoom import ClassRoom
from subject import Subject

class TimeTable:
    ''''''
    def __init__(self, day: str, start_time: str, end_time: str, subject: Subject, class_room: ClassRoom, id: str = ""):
        self.__id: str = id
        self.__day: str = day
        self.__start_time: str = start_time
        self.__end_time: str = end_time
        self.__subject: Subject = subject
        self.__class_room: ClassRoom = class_room

    def get_id(self):
        return self.__id

    def get_day(self):
        return self.__day

    def set_day(self, day: str):
        self.__day = day

    def get_start_time(self):
        return self.__start_time

    def set_start_time(self, start_time: str):
        self.__start_time = start_time

    def get_end_time(self):
        return self.__end_time

    def set_end_time(self, end_time: str):
        self.__end_time = end_time

    def get_subject(self) -> Subject:
            return self.__subject

    def set_subject(self, subject: Subject):
        self.__subject = subject

    def get_class_room(self) -> ClassRoom:
        return self.__class_room

    def set_class_room(self, class_room: ClassRoom):
        self.__class_room =class_room
