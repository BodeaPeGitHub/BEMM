import enum


class Condition(enum.Enum):
    severe_thinness = 0
    moderate_thinness = 1
    mild_thinness = 2
    normal = 3
    overweight = 4
    obese_class_1 = 5
    obese_class_2 = 6
    obese_class_3 = 7
