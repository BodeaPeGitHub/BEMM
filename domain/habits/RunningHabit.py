from domain.enums.ConditionEnum import Condition
from domain.enums.GenderEnum import Gender
from domain.enums.StatusEnum import Status


class RunningHabit:

    def __init__(self, condition, gender):
        self.__gender = gender
        self.__condition = condition
        self.__status = Status.not_started
        self.__minutes_ran = 0

    def __calculate_how_much_you_need_to_run(self):
        self.__running_time = 25
        if self.__gender == Gender.female:
            self.__running_time = 20
        if self.__condition in [Condition.mild_thinness, Condition.overweight]:
            self.__running_time -= 2
        if self.__condition in [Condition.moderate_thinness, Condition.obese_class_1]:
            self.__running_time -= 5
        if self.__condition in [Condition.severe_thinness, Condition.obese_class_2]:
            self.__running_time -= 7
        if self.__condition is Condition.obese_class_3:
            self.__running_time -= 10

    def running_time(self):
        self.__calculate_how_much_you_need_to_run()
        return self.__running_time

    def get_minutes_ran(self):
        return self.__minutes_ran

    def set_minutes_ran(self, new_minutes):
        self.__minutes_ran = new_minutes

    def get_status(self):
        return self.__status

    def set_status(self, new_status):
        self.__status = new_status
