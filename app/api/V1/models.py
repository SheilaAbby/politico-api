

party_list = []  # empty party list


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
