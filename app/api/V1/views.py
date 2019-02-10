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
              "message": " please fill all fields"}]})), 400


@app_route.route('/parties/<int:id>', methods=['GET'])  # pass the party id in the url
def get_single_political_party(id):
    """This endpoint returns a single political party"""
    single_political_party = party.getting_single_party(id)
    return make_response(jsonify(
        {
            "status": 200,
            "data": [{
                "id": single_political_party[0]["id"],  # return the first id  found in the list
                "name": single_political_party[0]["name"],
                "logoUrl": single_political_party[0]["logoUrl"]
            }]})), 200


@app_route.route('/parties', methods=['GET'])
def get_getting_all_parties():
    parties = party.getting_all_parties()  # class object 'party' calling the class method

    return make_response(jsonify({
        "status": 200,   # 200 status code for OK
        "data": parties
    })), 200


@app_route.route('/parties/<int:party_id>', methods=['PATCH'])
def edit_political_party(party_id):
    """"This route enables admin user
      - to edit political party passing party id as parameter"""

    data = request.get_json() # data is a parsed json data
    name_data = data.get('name') # get the party name from the parsed Json

    new_info = party.editing_party(party_id, name_data)
    return make_response(jsonify({"status": 200,
                                  "data": [{
                                          "id": party_id,
                                          "name": new_info[0]["name"],
                                          "message": "successfully updated name"
                                      }]})), 200

