class Habit:
    def __init__(self, idd, name, description, status):
        self.__id = idd
        self.__status = status
        self.__name = name
        self.__description = description

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_description(self):
        return self.__description

    def set_description(self, description):
        self.__description = description

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status

    def __eq__(self, other):
        return isinstance(other, Habit) and other.__id == self.__id

