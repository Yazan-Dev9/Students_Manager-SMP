from employee import Employee

class Manager(Employee):
    
    def __init__(self, name, id=None):
        super().__init__(name, id)
        self.__department = None
        self.__subordinates = []
        self.__reports_to = None
        