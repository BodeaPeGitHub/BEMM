from domain.ConditionEnum import Condition
from domain.GenderEnum import Gender
from domain.StatusEnum import Status


class SportingHabit:
    def __init__(self, gender, condition):
        self.__condition = condition
        self.__gender = gender
        self.__status = Status.not_started
        self.__actual_jumping_jacks = 0
        self.__actual_squats = 0
        self.__actual_crunches = 0
        self.__actual_push_ups = 0
        self.__calculate_workout()

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status

    def __calculate_workout(self):
        if self.__gender == Gender.female:
            if self.__condition == Condition.normal:
                self.__squats = 30
                self.__push_ups = 20
            if self.__condition == Condition.mild_thinness or self.__condition == Condition.overweight:
                self.__squats = 25
                self.__push_ups = 17
            if self.__condition == Condition.moderate_thinness or self.__condition == Condition.obese_class_1:
                self.__squats = 20
                self.__push_ups = 15
            if self.__condition == Condition.severe_thinness or self.__condition == Condition.obese_class_2:
                self.__squats = 15
                self.__push_ups = 13
            if self.__condition == Condition.obese_class_3:
                self.__squats = 13
                self.__push_ups = 10
        else:
            if self.__condition == Condition.normal:
                self.__squats = 50
            if self.__condition == Condition.mild_thinness or self.__condition == Condition.overweight:
                self.__squats = 45
            if self.__condition == Condition.moderate_thinness or self.__condition == Condition.obese_class_1:
                self.__squats = 40
            if self.__condition == Condition.severe_thinness or self.__condition == Condition.obese_class_2:
                self.__squats = 35
            if self.__condition == Condition.obese_class_3:
                self.__squats = 30
            self.__push_ups = self.__squats - 20
        self.__crunches = self.__squats
        self.__jumping_jacks = self.__squats

    def get_workout(self):
        return self.__jumping_jacks, self.__squats, self.__crunches, self.__push_ups

    def get_actual_workout(self):
        return self.__actual_jumping_jacks, self.__actual_squats, self.__actual_crunches, self.__actual_push_ups

    def set_jumping_jacks(self, jumping_jacks):
        self.__actual_jumping_jacks = jumping_jacks

    def set_squats(self, squats):
        self.__actual_squats = squats

    def set_crunches(self, crunches):
        self.__actual_crunches = crunches

    def set_push_ups(self, push_ups):
        self.__actual_push_ups = push_ups
