
import re
from marshmallow import ValidationError


def required(value):
    if isinstance(value, str):  # check if value is type string
        if not value.strip(' '):
            raise ValidationError('This parameter cannot be null')
        return value
    elif value:
        return value


def email(value):
    if not re.match(r"(^[a-zA-z0-9_.]+@[a-zA-z0-9]+\.[a-z]+$)", value):
        raise ValidationError('Invalid email format')
    return value
