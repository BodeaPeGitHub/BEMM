from domain.StatusEnum import Status
from datetime import date


class SleepingHabit:
    def __init__(self, birth_date, sleeping_habit_id):
        self.__status = Status.not_started
        self.__birth_date = birth_date
        self.__sleeping_habit_id = sleeping_habit_id
        self.__number_of_hours_slept = 0
        self.__number_of_hours = self.__compute_sleeping_time()

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status

    def get_sleeping_habit_id(self):
        return self.__sleeping_habit_id

    def get_hours_slept(self):
        return self.__number_of_hours_slept

    def add_slept_time(self, hours):
        self.__number_of_hours_slept = self.__number_of_hours_slept + hours

    def __compute_sleeping_time(self):
        age = self.__birth_date - date.today
        if age <= 13:
            return 9, 11
        if age <= 17:
            return 8, 10
        return 7, 9
