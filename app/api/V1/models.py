

party_list = []  # empty party list
office_list = []

users = {           # a nested dictionary

    "id": 32887889,
    "firstname": "Abigael",
    "lastname": "Kioko",
    "othername": "Sheila",
    "email": "sheila@gmail.com",
    "phoneNumber": "0700000001",
    "usertype": 1   # 1  is the default value for voter users
 }


class PartyModel:
    """This class represents the party model data"""

    def __init__(self):  # constructor
        self.db = party_list

    # this method handles creation of a new party and saving it to party list
    def creating_party(self, data):

        """creates new political party"""
        new_political_party = {
            "id": len(self.db) + 1,
            "name": data.get('name'),
            "hqaddress": data.get('hqaddress'),
            "logourl": data.get('logourl')

        }
        self.db.append(new_political_party)  # add to the party list
        return new_political_party

    def check_party_exists(self, key, data):
        """
        Check that data being posted does not exist
        :param key:
        :param data:
        :return:
        """
        party_exists = [party for party in party_list if data == party[key]] # party_exists array stores similar  values
        return len(party_exists) > 0  # if there exists similar values this statement is True,


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


class UserModel:
    def __init__(self):
        self.db = users

    def signup_user(self, data):
        """
        process of registering a user to the system.only non admins register
        :param data:
        :return:
        """
        new_user = {
            "id": data.get('id'),
            "firstname": data.get('firstname'),
            "lastname": data.get('lastname'),
            "othername": data.get('othername'),
            "email": data.get('email'),
            "phoneNumber": data.get('phoneNumber'),
            "isadmin": data.get('usertype')

        }
        self.db.append(new_user)
        return new_user


