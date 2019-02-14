from marshmallow import Schema, fields, post_dump
from ..utils.validations import required, email
from  app.api.V1.models import UserModel,PartyModel,OfficeModel


class OfficeSchema(Schema):
    """
    validates office object schema
    """
    id = fields.Int(dump_only=True)
    type = fields.Str(required=False)
    name = fields.Str(required=True, validate=(required()))


class UserSchema(Schema):
    """
    User class to validate schema for user object
    """
    nationalID = fields.Int(dump_only=True)
    firstname = fields.Str(required=True, validate=(required()))
    lastname = fields.Str(required=True, validate=(required()))
    othername = fields.Str(required=False)
    password = fields.Str(required=True)
    phoneNumber = fields.Str(required=True, validate=(required()))
    email = fields.Email(required=True, validate=(email()))
    passportUrl = fields.Str(required=False)
    isAdmin = fields.Bool(dump_only=True)


class PoliticalPartySchema(Schema):
    """
    class to validate political party object schema
    """
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=(required()))
    hqAddress = fields.Str(required=False)
    logoUrl = fields.Str(required=False)
