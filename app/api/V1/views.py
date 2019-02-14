from flask import Blueprint, request, make_response, jsonify, abort
from app.api.V1.models import PartyModel, OfficeModel, UserModel
from utils.schemas import PartySchema

# make a Blueprint route called app_route
app_route = Blueprint('politico-v1', __name__)
party = PartyModel()  # creates an instance of the PartyModel class
office = OfficeModel()
user = UserModel


#  creating political parties CRUD endpoints
@app_route.route('/parties', methods=['POST'])
def post_party():
    """"This endpoint enables admin user
      - to create political party"""

    party_req_data = request.get_json()

    if not party_req_data:
        abort(make_response(jsonify({
            "status": 400,
            "message": 'Please fill all fields'
        }), 400))

    data, errors = PartySchema().load(party_req_data)  # parses a JSON object(party_req_data)
    if errors:
        abort(make_response(jsonify({
            "status": 422,  # 422 Unprocessable Entity - data in bad format
            "message": "Incorrect data,Try again",
            "errors": errors

        }), 422))

    new_party_data = party.creating_party(data)
    response = PartySchema().dump(new_party_data).data  # dump method changes the python object to JSON

    return make_response(jsonify({
        "status": 201,
        "data": [{
          "message": "Success! Party Created",
          "new party": response
        }],
        })), 201


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
def get_all_parties():
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


@app_route.route('/parties/<int:id>', methods=['DELETE'])
def delete_political_party(id):
    party.deleting_a_party(id)
    return make_response(jsonify({
        "status": 200,
        "data": [{
            "message": "Successfully deleted party"
        }]
    })), 200


# creating office CRUD endpoints
@app_route.route('/offices', methods=['POST'])
def post_office():
    """
    Endpoint enables an admin user to  create an office
    :return: added office details with a success message
    """
    office_data = request.get_json()  # parse json
    office_type = office_data.get('type')
    name = office_data.get('name')

    if name and office_type:  # when both fields are filled return a 201, success code
        new_office_data = office.creating_office(name, office_type)
        return make_response(jsonify({
            "status": 201,
            "data": [{
              "id": new_office_data["id"],
              "name": new_office_data["name"],
              "type": new_office_data["type"]
            }],
            })), 201

    else:          # else if fields are blank return a 400, bad request
        return make_response(jsonify({
            "status": 400,
            "data": [{
              "message": " please fill all fields"}]})), 400


@app_route.route('/offices', methods=['GET'])
def get_all_offices():
    offices = office.getting_all_offices()
    return make_response(jsonify({
        "status": 200,
        "data": offices
    }))


@app_route.route('/offices/<int:id>', methods=['GET'])
def get_single_office(id):
    """
    This endpoint enables a user to get a single office item by an id
    :param id:
    :return: specific office item
    """
    single_office = office.getting_single_office(id)
    return make_response(jsonify({
        "status": 200,
        "data": [{
            "id": single_office[0]['id'],
            "type": single_office[0]['type'],
            "name": single_office[0]['name']
        }]
    })), 200


@app_route.route('/users', methods=['POST'])
def add_users():
    """
    This endpoint handles creating new users
    :return:
    """
    user_req_data = request.get_json()

