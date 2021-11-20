from domain.User import User


class UserService:
    def __init__(self, user_repository, user_validator):
        self.__user_validator = user_validator
        self.__user_repository = user_repository

    def save(self, username, first_name, last_name, gender, birthday, weight, height):
        user = User(username, first_name, last_name, gender, birthday, weight, height)
        self.__user_validator.validate(user)
        self.__user_repository.save(user)

    def __return_data(self, user_id):
        user = self.__user_repository.find_one(user_id)
        username = user.get_username()
        first_name = user.get_first_name()
        last_name = user.get_last_name()
        gender = user.get_gender()
        birthday = user.get_birthday()
        weight = user.get_weight()
        height = user.get_height()
        return username, first_name, last_name, gender, birthday, weight, height

    def __update(self, user):
        self.__user_validator.validate(user)
        self.__user_repository.update(user)

    def update_first_name(self, user_id, first_name):
        username, _, last_name, gender, birthday, weight, height = self.__return_data(user_id)
        user = User(username, first_name, last_name, gender, birthday, weight, height)
        user.set_user_id(user_id)
        self.__update(user)

    def update_last_name(self, user_id, last_name):
        username, first_name, _, gender, birthday, weight, height = self.__return_data(user_id)
        user = User(username, first_name, last_name, gender, birthday, weight, height)
        user.set_user_id(user_id)
        self.__update(user)

    def update_weight(self, user_id, weight):
        username, first_name, last_name, gender, birthday, _, height = self.__return_data(user_id)
        user = User(username, first_name, last_name, gender, birthday, weight, height)
        user.set_user_id(user_id)
        self.__update(user)

    def update_height(self, user_id, height):
        username, first_name, last_name, gender, birthday, weight, _ = self.__return_data(user_id)
        user = User(username, first_name, last_name, gender, birthday, weight, height)
        user.set_user_id(user_id)
        self.__update(user)

    def delete(self, user_id):
        user = User("", "", "", "", "", "", "")
        user.set_user_id(user_id)
        self.__user_repository.delete(user)

    def find_one(self, user_id):
        user = User("", "", "", "", "", "", "")
        user.set_user_id(user_id)
        self.__user_repository.find_one(user)

    def find_all(self):
        self.__user_repository.find_all()

    def add_glasses(self, user_id):
        user = self.__user_repository.find_one(user_id)
        self.__user_repository\
            .update_attribute("glasses_drank", user.get_water_habit().get_number_of_glasses_drunk() + 1, user_id)
