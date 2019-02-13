from marshmallow import Schema, fields, pprint

from utils.validators import required_input, is_valid_phone, is_valid_id, is_admin_user, is_voter_user

from app.api.V1.models import PartyModel, OfficeModel

party = PartyModel() # instance of Party model class


class PartySchema(Schema):
    """
    class validates a Party object
    """
    id = fields.Int(dump_only=True)  # specifies read only fields
    name = fields.Str(required=True, validate=(required_input()))
    hqaddress = fields.Str(required=False)
    logourl = fields.Url(required=False)


class OfficeSchema(Schema):
    """
    class validates an office data
    """
    name = fields.Str(required=True)
    type = fields.Str(required=True)


class UserSchema(Schema):
    id = fields.Int(validate=is_valid_id())
    firstname = fields.Str(required=True, validate=(required_input()))
    lastname = fields.Str(required=True, validate=(required_input()))
    othername = fields.Str(required=True, validate=required_input())
    email = fields.Email(required=True)
    phoneNumber = fields.Str(required=True,  validate=(is_valid_phone(), required_input()))
    passportUrl = fields.Url(required=False)
    isadmin = fields.Int(dump_only=True, validate=(is_admin_user()))  # admin user type is value 1
    voter = fields.Int(dump_only=True, validate = (is_voter_user()))  # voter user type is value 2
    candidate = fields.Int(dump_only=True)  # candidate user type is value 3

