from flask import Blueprint, request, make_response, jsonify

from app.api.V1.models import PartyModel

# make a Blueprint route called app_route
app_route = Blueprint('politico-v1', __name__)
party = PartyModel()  # creates an instance of the PartyModel class


@app_route.route('/parties', methods=['POST'])
def post_party():
    """"This endpoint enables admin user
      - to create political party"""

    data = request.get_json()
    name = data.get('name')
    hdaddress = data.get('hqAddress')
    logourl = data.get('logoUrl')

    if name and hdaddress and logourl:  # when both fields are filled return a 201, success code
        new_party_data = party.creating_party(name, hdaddress, logourl)
        return make_response(jsonify({
            "status": 201,
            "data": [{
              "id": new_party_data["id"],
              "name": new_party_data["name"]
            }],
            })), 201

    else:          # else if fields are blank return a 400, bad request
        return make_response(jsonify({
            "status": 400,
            "data": [{
              "message": "some required fields missing"}]})), 400


