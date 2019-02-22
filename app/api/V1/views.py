from flask import Blueprint, request, make_response, jsonify
from .models import PartyModel, OfficeModel, UserModel
from utils.data_schemas import UserSchema
from flask_jwt_extended import create_access_token, create_refresh_token


# make a Blueprint route called app_route
app_route = Blueprint('politico-v1', __name__, url_prefix='/api/v1')
party = PartyModel()  # creates an instance of the PartyModel class
office = OfficeModel()
user = UserModel()


@app_route.route('/index', methods=['GET'])
def get_index_page():
        return jsonify({
            "status": 200,
            "message": "WELCOME TO POLITICO-API, VISIT https://politico-api-eletions.herokuapp.com/api/v1"
         })
#  creating political parties CRUD endpoints


@app_route.route('/parties', methods=['POST'])
def post_party():
    """"This endpoint enables admin user
      - to create political party"""

    data = request.get_json()
    name = data.get('name')
    logourl = data.get('logoUrl')
    hqaddress = data.get('hqAddress')

    if name and hqaddress and logourl:  # when both fields are filled return a 201, success code
        new_party_data = party.creating_party(name, logourl, hqaddress)
        return make_response(jsonify({
            "status": 201,
            "message": "party created",
            "data": [{
              "id": new_party_data["id"],
              "name": new_party_data["name"],
              "logoUrl": new_party_data["logoUrl"],
              "hqAddress": new_party_data["hqAddress"]
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


@app_route.route('/parties/<int:int_id>', methods=['DELETE'])
def delete_political_party(int_id):
    """
    delete a political party
    :param int_id
    :return:
    """
    # find party by id
    party_to_delete = party.getting_single_party(int_id)
    print(party_to_delete)
    if party_to_delete:  # if that party exists
        party.deleting_a_party(int_id)
        return make_response(jsonify({
            "status": 200,
            "data": [{
                "message": "Successfully deleted party"
            }]
        })), 200
    else:
        return make_response(jsonify({
            "status": 400,
            "data": [{
                "message": "Deleted"
            }]
        }))


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
        new_office_data = office.creating_office(office_type, name)
        return make_response(jsonify({
            "status": 201,
            "data": [{
              "id": new_office_data["id"],
              "type": new_office_data["type"],
              "name": new_office_data["name"],

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
    if single_office:  # if an office with the passed id exists
        return make_response(jsonify({
            "status": 200,
            "data": [{
                "id": single_office[0]['id'],
                "type": single_office[0]['type'],
                "name": single_office[0]['name']
                }]
            })), 200

    else:  # the is does not exist, throw 400 error
        return make_response(jsonify({
            "status": 400,
            "msg": "An office with that ID does not exist"
        }))


@app_route.route('/users', methods=['POST'])
def post_users():
    user_data = request.get_json()
    if not user_data:
        return jsonify({
            "status": 400,
            "message": "Provide all required data"
        }), 400

    data, errors = UserSchema().load(user_data)  # pass the user data for validation

    if errors:
        return jsonify({
            "status": 400,
            "message": "Invalid data!"
        })

    if user.check_if_user_exists('nationalID', data['nationalID']):
        return jsonify({
            "status": 409,
            "message": "The national ID already exists"
        }), 409

    if user.check_if_user_exists('phoneNumber', data['phoneNumber']):
        return jsonify({
            "status": 409,
            "message": "User with that phone number already exists"
        })
    if user.check_if_user_exists('email', data['email']):
        return jsonify({
            "status": 409,
            "message": "User with that email exists"
        })
    new_user = user.register(data)
    response = UserSchema(exclude=['password']).dump(new_user).data

    #  generate access tokens
    access_token = create_access_token(identity=new_user['id'], fresh=True)
    refresh_token = create_refresh_token(identity=new_user['id'])
    return jsonify({
        "status": 201,
        "data": [{
            "citizen": response,
            "message": "Registered successfully!"
        }]
    })
