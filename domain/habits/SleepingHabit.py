<<<<<<< HEAD:domain/SleepingHabit.py
import math
from BEMM.domain.StatusEnum import Status
import StatusEnum
=======
import datetime

from domain.enums.StatusEnum import Status
>>>>>>> 2a842c29ae90c71fd95d22498e6ff2456bc9ac8c:domain/habits/SleepingHabit.py
from datetime import date

class SleepingHabit:
<<<<<<< HEAD:domain/SleepingHabit.py
    def __init__(self,birth_date,sleeping_habit_id):
=======
    def __init__(self, birth_date):
>>>>>>> 2a842c29ae90c71fd95d22498e6ff2456bc9ac8c:domain/habits/SleepingHabit.py
        self.__status = Status.not_started
        self.__birth_date = birth_date
        self.__number_of_hours_slept = 0
        self.__number_of_hours = self.__compute_sleeping_time()

    def get_status(self):
        return self.__status
    
    def set_status(self,status):
        self.__status = status

    def get_hours_slept(self):
        return self.__number_of_hours_slept

<<<<<<< HEAD:domain/SleepingHabit.py
    def add_slept_time(self,hours):
        self.__number_of_hours_slept = self.__number_of_hours_slept + hours

    def __compute_sleeping_time(self):
        age = self.__birth_date - date.today
        if self.__age <= 13:
            return 9,11
        if self.__age <= 17:
            return 8,10
        return 7,9
=======
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
>>>>>>> 2a842c29ae90c71fd95d22498e6ff2456bc9ac8c:domain/habits/SleepingHabit.py
