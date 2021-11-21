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

    def find_one_by_username(self, username):
        return self.__user_repository.find_one_by_username(username)

    def add_glasses(self, user_id):
        user = self.__user_repository.find_one(user_id)
        self.__user_repository.update_attribute("glasses_drank", user.get_water_habit().get_number_of_glasses_drunk() + 1, user_id)

    def return_number_of_glasses(self, user_id):
        user = self.__user_repository.find_one(user_id)
        return user.get_water_habit().get_number_of_glasses()

    def achieved_water_habit(self, user_id):
        user = self.__user_repository.find_one(user_id)
        return user.get_water_habit().get_number_of_glasses() <= user.get_water_habit().get_number_of_glasses_drunk()

    def add_running_time(self, user_id, running_time):
        user = self.__user_repository.find_one(user_id)
        self.__user_repository.update_attribute("minutes_run", user.get_running_habit().get_minutes_ran() + running_time, user_id)

    def return_running_time(self, user_id):
        user = self.__user_repository.find_one(user_id)
        return user.get_running_habit().running_time()

    def achieved_running_habit(self, user_id):
        user = self.__user_repository.find_one(user_id)
        return user.get_running_habit().running_time() <= user.get_running_habit().get_minutes_ran()

    def add_jumping_jacks(self, user_id, nr_of_jumping_jacks):
        user = self.__user_repository.find_one(user_id)
        self.__user_repository.update_attribute("jumping_jacks", user.get_sporting_habit().get_actual_workout()[0] + nr_of_jumping_jacks, user_id)

    def add_squats(self, user_id, nr_of_squats):
        user = self.__user_repository.find_one(user_id)
        self.__user_repository.update_attribute("squats", user.get_sporting_habit().get_actual_workout()[1] + nr_of_squats, user_id)

    def add_crunches(self, user_id, nr_of_crunches):
        user = self.__user_repository.find_one(user_id)
        self.__user_repository.update_attribute("crunches", user.get_sporting_habit().get_actual_workout()[2] + nr_of_crunches, user_id)

    def add_push_ups(self, user_id, nr_of_push_ups):
        user = self.__user_repository.find_one(user_id)
        self.__user_repository.update_attribute("push_ups", user.get_sporting_habit().get_actual_workout()[3] + nr_of_push_ups, user_id)

    def achieved_sport_habit(self, user_id):
        user = self.__user_repository.find_one(user_id)
        return user.get_sporting_habit().get_actual_workout() >= user.get_sporting_habit().get_workout()

    def return_sleeping_habit(self, user_id):
        user = self.__user_repository.find_one(user_id)
        return user.get_sleeping_habit().get_number_of_hours()

    def calculate_when_to_wake_up(self, user_id, time):
        pass

    def calculate_when_to_go_to_sleep(self, user_id, time):
        pass



