import math
from domain.enums.StatusEnum import Status


class WaterHabit:
    def __init__(self, weight):
        self.__status = Status.not_started
        self.__number_of_glassed_drunk = 0
        self.__weight = weight
        self.__calculate_number_of_glasses()

    def __calculate_number_of_glasses(self):
        self.__number_of_glasses = math.ceil((self.__weight * 2.2 * 67) // 8)

    def get_status(self):
        return self.__status

    def get_number_of_glasses(self):
        return self.__number_of_glasses

    def get_number_of_glasses_drunk(self):
        return self.__number_of_glassed_drunk

    def set_status(self, status):
        self.__status = status

    def set_glass_of_water_drunk(self, new_number):
        self.__number_of_glassed_drunk = new_number
