from domain.exceptions.Exceptions import ValidationException


class UserValidator:
    def __init__(self):

    def validate(self):
        error = ""
        if self.__user.get_first_name() == "":
            error += "First name is a required field.\n"
        if self.__user.get_last_name() == "":
            error += "Last name is a required field.\n"
        if self.__user.get_username() == "":
            error += "Username is a required field.\n"
        if self.__user.get_height() < 120 or self.__user.get_height() > 250:
            error += "Invalid height. It has to be between 120cm and 250cm.\n"
        if self.__user.get_weight() < 30 or self.__user.get_weight() > 300:
            error += "Invalid weight. It has to be between 30kg and 300kg.\n"
        if error != "":
            raise ValidationException(error)
