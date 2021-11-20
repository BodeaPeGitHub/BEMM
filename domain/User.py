class User:
    def __init__(self, username, first_name, last_name, gender, birthday, weight, height):
        self.__user_id = 0
        self.__username = username
        self.__first_name = first_name
        self.__last_name = last_name
        self.gender = gender
        self.__birthday = birthday
        self.__height = height
        self.__weight = weight
        self.__bmi = (weight / (height * height)) * 10000
        self.__calculate_condition()
        self.__habits = []

    def __calculate_condition(self):
        if self.__bmi < 16:
            self.__condition = "Severe Thinness"
        elif self.__bmi < 17:
            self.__condition = "Moderate Thinness"
        elif self.__bmi < 18.5:
            self.__condition = "Mild Thinness"
        elif self.__bmi < 25:
            self.__condition = "Normal"
        elif self.__bmi < 30:
            self.__condition = "Overweight"
        elif self.__bmi < 35:
            self.__condition = "Obese Class I"
        elif self.__bmi < 40:
            self.__condition = "Obese Class II"
        else:
            self.__condition = "Obese Class III"

    def __add_habit(self, habit):
        self.__habits.append(habit)

    def get_user_id(self):
        return self.__user_id

    def get_username(self):
        return self.__username

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_gender(self):
        return self.gender

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

    def __eq__(self, o):
        return isinstance(o, User) and self.__user_id == o.__user_id and self.__username == o.__username






