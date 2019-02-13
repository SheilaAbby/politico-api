from marshmallow import Schema, fields, pprint

from utils.validators import required_input

from app.api.V1.models import PartyModel, OfficeModel

party = PartyModel() # instance of Party model class


class PartySchema(Schema):
    """
    class validates a Party object
    """
    id = fields.Int(dump_only=True)  # specifies read only fields
    name = fields.Str(required=True, validate=(required_input))
    hqaddress = fields.Str(required=False)
    logourl = fields.Url(required=False)
