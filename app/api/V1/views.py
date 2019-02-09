from flask import Blueprint, request, make_response, jsonify

from app.api.V1.models import PartyModel

# make a Blueprint route called app_route
app_route = Blueprint('politico-v1', __name__)


@app_route.route('/parties', methods=['POST'])
def post_party():  # method handles posting of data
    data = request.get_json()

    name = data["name"]  # from the party_data get name value
    hqaddress = data["hqAddress"]
    logourl = data["logoUrl"]  # from the party_data get logourl value

    party = PartyModel(name=name, logourl=logourl, hqaddress=hqaddress)

    party.creating_party()

    return make_response(jsonify({
        "status": 201,
        "message": "Political Party created successfully",
        "data": data
    })), 201

