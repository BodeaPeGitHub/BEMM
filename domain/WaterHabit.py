import math


class WaterHabit:
    def __init__(self, water_habit_id, number_of_glasses, weight):
        self.__weight = weight
        self.__number_of_glassed_drunk = 0
        self.__number_of_glasses = number_of_glasses
        self.__water_habit_id = water_habit_id
        #self.__status =
        self.__calculate_number_of_glasses()

    def __calculate_number_of_glasses(self):
        self.__number_of_glasses = math.ceil((self.__weight * 2.2 * 67) // 8)

    def get_water_habit_id(self):
        return self.__water_habit_id
