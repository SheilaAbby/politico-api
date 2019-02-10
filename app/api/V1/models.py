

party_list = []  # empty party list
office_list = []


class PartyModel:
    """This class represents the party model data"""

    def __init__(self):  # constructor
        self.db = party_list

    # this method handles creation of a new party and saving it to party list
    def creating_party(self, new_party_name, new_party_hdaddress, new_party_logo):
        """creates new political party"""
        new_political_party = {
            "id": len(self.db) + 1,
            "name": new_party_name,
            "hqAddress": new_party_hdaddress,
            "logoUrl": new_party_logo

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

    def getting_single_office(self):
        pass

    def editing_a_office(self):
        pass

    def deleting_a_office(self):
        pass



