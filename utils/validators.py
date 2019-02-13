import re
from marshmallow import ValidationError


def required_input(input):
    """
    Ensure no blank fields are submitted
    :param input:
    :return:
    """

    if isinstance(input, str):
        if not input:   # if input is empty
            raise ValidationError('Field cannot be Empty')
        return input
    elif input:
        return input


