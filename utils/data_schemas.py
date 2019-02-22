from .validations import required, email, password
from marshmallow import Schema, fields, post_dump
from  app.api.V1.models import UserModel,PartyModel,OfficeModel


class OfficeSchema(Schema):
    """
    validates office object schema
    """
    id = fields.Int(dump_only=True)
    type = fields.Str(required=False)
    name = fields.Str(required=True, validate=(required))


class UserSchema(Schema):
    """
    User class to validate schema for user object
    """
    id = fields.Int(dump_only=True)
    nationalID = fields.Int(dump_only=False)
    firstname = fields.Str(required=True, validate=(required))
    lastname = fields.Str(required=True, validate=(required))
    othername = fields.Str(required=False)
    password = fields.Str(required=True, validate=(password))
    phoneNumber = fields.Str(required=True, validate=(required))
    email = fields.Email(required=True, validate=(email))
    passportUrl = fields.Str(required=False)
    createdOn = fields.Int(dump_only=True)
    isAdmin = fields.Bool(dump_only=True)


class PoliticalPartySchema(Schema):
    """
    class to validate political party object schema
    """
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=(required))
    hqAddress = fields.Str(required=False)
    logoUrl = fields.Str(required=False)
