
from werkzeug.security import generate_password_hash, check_password_hash
from utils.generate_id import generate_id
from datetime import datetime


revoked_tokens = []


class RevokedTokenModel(object):
    """
    Model class for revoked tokens
    """
    def add(self, jti):
        """
        method to save token id
        """
        revoked_tokens.append(jti)

    def is_blacklisted(self, jti):
        """
        method to check if token id is blacklisted
        """
        return bool(jti in revoked_tokens)


party_list = []  # empty party list
office_list = []
users = []


class PartyModel:
    """This class represents the party model data"""

    def __init__(self):  # constructor
        self.db = party_list

    # this method handles creation of a new party and saving it to party list
    def creating_party(self, new_party_name, new_party_logo,  new_party_hqaddress):
        """creates new political party"""
        new_political_party = {
            "id": len(self.db) + 1,
            "name": new_party_name,
            "logoUrl": new_party_logo,
            "hqAddress": new_party_hqaddress
        }

        self.db.append(new_political_party)  # add to the party list
        return new_political_party

    def getting_single_party(self, id):
        """finds a single party by it id and returns it"""
        single_party = [party for party in self.db if party['id'] == id]
        return single_party

    def getting_all_parties(self):
        """

        :return: a list of all political parties
        """
        return party_list

    def editing_party(self, id, name):
        """update party information for particular ID"""

        party_to_edit_name = [party for party in party_list if party['id'] == id]   
        party_to_edit_name[0]['name'] = name

        return party_to_edit_name

    def deleting_a_party(self, id):  # search for a party to delete by id
        self.db.pop(id - 1)  # takes a single argument (index) and removes the item present at that index.
        return self.db


class OfficeModel:
    """
    This class handles the Office data model
    """

    def __init__(self):
        """
        A constructor
        """
        self.db = office_list  # empty offices list

    def creating_office(self, office_type, name):
        """
        Creates an office
        :param office_type: can be senate_office,national_government,county_office,local_government
        :param name: can be 'office of the senate', 'office of the president', 'MCA','Office of the Governor' etc
        :return: a new list with the office added
        """
        new_political_office = {
            "id": len(self.db) + 1,
            "name": name,
            "type": office_type
        }

        self.db.append(new_political_office)
        return new_political_office

    def getting_all_offices(self):
        """

        :return: a list of all offices
        """
        return office_list

    def getting_single_office(self, id):
        """

        :param id:
        :return: a single office
        """
        single_office = [office for office in office_list if office['id'] == id]
        return single_office

    def editing_an_office(self, id, name):

        """
        :param id: id of the specific office name to be edited
        :return: edited office details
        """
        office_to_edit_name = [office for office in office_list if office['id'] == id]
        office_to_edit_name[0]['name'] = name

        return office_to_edit_name

    def deleting_a_office(self, id):
        """

        :param id: id of the office to be deleted
        :return: office_list without the office deleted
        """
        self.db.pop(id - 1)  # takes a single argument (index) and removes the item present at that index.
        return self.db


class UserModel(object):
    """
      Model class for user object
    """

    def register(self, data):
        """
          method to register a new user
        """
        data['id'] = generate_id(users)  # get the id
        data['password'] = generate_password_hash('password')  # generate pass
        data['createdOn']: datetime.now()  # current time
        data['isAdmin']: False  # by default isAdmin is false

        users.append(data)  # update the empty dict with new data
        return data

    def check_if_user_exists(self, key, value):
        """
         checks if a user exists - match any key with value
        """
        existing_user = [user for user in users if value == user[key]]
        return len(existing_user) > 0  # if false user does not exist

    def find_user_by_national_id(self, key, nationalID):
        """
          method to find a user by ID
        """
        user_with_id = [user for user in users if user['nationalID'] == nationalID]
        return user_with_id[0]  # get the first user to be found with that id

    def check_password(self, hash, password):
        """
         checks if the passwords match before registering user
        """

        return check_password_hash(hash, password)
