import datetime
import math

from domain.enums.StatusEnum import Status


class SleepingHabit:
    def __init__(self, birth_date):
        self.__status = Status.not_started
        self.__birth_date = birth_date
        self.__number_of_hours_slept = False
        self.__number_of_hours = self.__compute_sleeping_time()

    def get_number_of_hours(self):
        return self.__number_of_hours

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status

    def get_hours_slept(self):
        return self.__number_of_hours_slept

    def set_number_hour_slept(self, new_number):
        self.__number_of_hours_slept = new_number

    def add_slept_time(self, hours):
        self.__number_of_hours_slept = self.__number_of_hours_slept + hours

    def __compute_sleeping_time(self):
        today = datetime.date.today()
        born = self.__birth_date
        age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        if age <= 13:
            return 9, 11
        if age <= 17:
            return 8, 10
        return 7, 9
