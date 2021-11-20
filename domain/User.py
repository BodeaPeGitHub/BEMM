import datetime

from domain.habits.RunningHabit import RunningHabit
from domain.habits.SleepingHabit import SleepingHabit
from domain.habits.SportingHabit import SportingHabit
from domain.habits.WaterHabit import WaterHabit
from domain.enums.ConditionEnum import Condition


class User:

    def __init__(self, username, first_name, last_name, gender, birthday, weight, height):
        self.__user_id = 0
        self.__username = username
        self.__first_name = first_name
        self.__last_name = last_name
        self.__gender = gender
        self.__birthday = birthday
        self.__height = int(height)
        self.__weight = int(weight)
        self.__bmi = (self.__weight / (self.__height * self.__height)) * 10000
        self.__running_habit = None
        self.__sleeping_habit = None
        self.__sporting_habit = None
        self.__water_habit = None
        self.__calculate_condition()
        self.__adding_habits()

    def __adding_habits(self):
        self.__running_habit = RunningHabit(self.__condition, self.__gender)
        self.__sleeping_habit = SleepingHabit(self.__birthday)
        self.__sporting_habit = SportingHabit(self.__gender, self.__condition)
        self.__water_habit = WaterHabit(self.__weight)

    def get_running_habit(self):
        return self.__running_habit

    def get_sleeping_habit(self):
        return self.__sleeping_habit

    def get_sporting_habit(self):
        return self.__sporting_habit

    def get_water_habit(self):
        return self.__water_habit

    def __calculate_condition(self):
        if self.__bmi < 16:
            self.__condition = Condition.severe_thinness
        elif self.__bmi < 17:
            self.__condition = Condition.moderate_thinness
        elif self.__bmi < 18.5:
            self.__condition = Condition.mild_thinness
        elif self.__bmi < 25:
            self.__condition = Condition.normal
        elif self.__bmi < 30:
            self.__condition = Condition.overweight
        elif self.__bmi < 35:
            self.__condition = Condition.obese_class_1
        elif self.__bmi < 40:
            self.__condition = Condition.obese_class_2
        else:
            self.__condition = Condition.obese_class_3

    def get_user_id(self):
        return self.__user_id

    def get_username(self):
        return self.__username

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_gender(self):
        return self.__gender

    def get_birthday(self):
        return self.__birthday

    def get_weight(self):
        return self.__weight

    def get_height(self):
        return self.__height

    def get_bmi(self):
        return self.__bmi

    def get_condition(self):
        return self.__condition

    def set_user_id(self, user_id):
        self.__user_id = user_id

    def set_username(self, username):
        self.__username = username

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_weight(self, weight):
        self.__weight = weight
        self.__calculate_condition()

    def set_height(self, height):
        self.__height = height
        self.__calculate_condition()

    def __str__(self):
        jumping_jacks, squats, crunches, push_ups = self.__sporting_habit.get_actual_workout()
        return f"{self.__user_id} | {self.__username} | {self.__first_name} | {self.__last_name} | {self.__gender} | {self.__height} | {self.__birthday} | {self.__weight} | {self.__running_habit.get_minutes_ran()} |  {self.__sleeping_habit.get_hours_slept()} | {self.__water_habit.get_number_of_glasses_drunk()} | {jumping_jacks} | {squats} | {crunches} | {push_ups}"

    def __eq__(self, o):
        return isinstance(o, User) and self.__user_id == o.__user_id and self.__username == o.__username






