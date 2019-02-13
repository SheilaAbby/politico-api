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


def is_admin_user(admin_value):
    """
    Function checks the if the passed value is 1 for isadmin field
    :param admin_value:
    :return:
    """
    if isinstance(admin_value, int):
        if admin_value != 1:
            raise ValidationError('Invalid value')
        return admin_value
    elif admin_value:
        return admin_value


def is_voter_user(voter_value):
    """
    Function checks  if the passed value is 2 for voter field
    :param voter_value:
    :return:
    """
    if isinstance(voter_value, int):
        if voter_value != 2:
            raise ValidationError('Invalid value')
        return voter_value
    elif voter_value:
        return voter_value


def is_valid_phone(phone_number):
    """Check if phone number is kenyan format."""

    if re.match(r"^(?:254|\+254|0)?(7(?:(?:[12][0-9])|(?:0[0-8])|(9[0-2]))[0-9]{6})$",
                phone_number):
        return True
    return False

