from marshmallow import ValidationError
import re  # use regex


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


def password(password):
    """
    Ensurepasses password is strong
    :param password:
    :return:
    """
    if not re.match(r'[A-Za-z0-9@#$%^&+=]{8,}', password):
        raise ValidationError('Password not Strong')
    return password


def is_valid_url(value):
    """Check if the logoUrl is a valid url."""

    if re.match(r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)",
                value):
        return True
    return False


def is_valid_date(value):
    """Check if date is valid."""

    if re.match(
            r"^(?:(?:31(\/|-|\.)(?:0?[13578]|1[02]))\1|(?:(?:29|30)(\/|-|\.)"
            r"(?:0?[1,3-9]|1[0-2])\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/|-|\.)"
            r"0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|"
            r"(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/|-|\.)"
            r"(?:(?:0?[1-9])|(?:1[0-2]))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})$",
            value):
        return True
    return False


def is_valid_phone(value):
    """Check if phone number is a valid kenyan phone number."""

    if re.match(r"^(?:254|\+254|0)?(7(?:(?:[12][0-9])|(?:0[0-8])|(9[0-2]))[0-9]{6})$",
                value):
        return True
    return False
