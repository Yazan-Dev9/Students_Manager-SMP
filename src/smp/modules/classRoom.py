class ClassRoom:
    ''''''
    def __init__(self, name: str = "", id: str = ""):
        self.__id = id
        self.__name = name
        self.__capacity: int = 0
        self.__grade: str = ""

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def set_name(self, name: str):
        self.__name = name

    def get_grade(self):
        return self.__grade

    def set_grade(self, grade: str):
        self.__grade = grade

    def get_capacity(self):
        return self.__capacity

    def set_capacity(self, capacity: int):
        self.__capacity = capacity

    def save(self):
        pass