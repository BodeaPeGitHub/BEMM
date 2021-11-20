from domain.exceptions.Exceptions import ValidationException


class UserValidator:
    def validate(self,user):
        error = ""
        if user.get_first_name() == "":
            error += "First name is a required field.\n"
        if user.get_last_name() == "":
            error += "Last name is a required field.\n"
        if user.get_username() == "":
            error += "Username is a required field.\n"
        if user.get_height() < 120 or user.get_height() > 250:
            error += "Invalid height. It has to be between 120cm and 250cm.\n"
        if user.get_weight() < 30 or user.get_weight() > 300:
            error += "Invalid weight. It has to be between 30kg and 300kg.\n"
        if error != "":
            raise ValidationException(error)
