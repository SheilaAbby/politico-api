import re
from marshmallow import ValidationError


def required_input(input):
    """
    Ensure no blank fields are submitted
    :param input:
    :return:
    """

    if isinstance(input, str): # isintance checks whether the passes id_number is an int
        if not input:   # if input is empty
            raise ValidationError('Field cannot be Empty')
        return input
    elif input:
        return input


def user_type(value):
    """
    checks the type of user
    :param value:
    :return:
    """
    type_list = [1, 2, 3]  # list containing user type values 1-voter 2-admin 3-candidate

    if isinstance(value, int):  # check the passes value is a string
        if value not in type_list:  # when posting, by default the value passed for user type should be 1
            raise ValidationError('Unknown User Type')
        return value
    elif value:
        return value


def is_valid_id(id_number):
    """
    Validates that the passed id is 8 digits long
    :param id_number:
    :return:
    """
    if isinstance(id_number, int):  # isintance checks whether the passes id_number is an int
        if len(id_number) != 8:
            raise ValidationError('ID number must be 8 digits long')
        return id_number
    elif id_number:
        return id_number


def is_valid_phone(phone_number):
    """Check if phone number is kenyan format."""

    if re.match(r"^(?:254|\+254|0)?(7(?:(?:[12][0-9])|(?:0[0-8])|(9[0-2]))[0-9]{6})$",
                phone_number):
        return True
    return False

