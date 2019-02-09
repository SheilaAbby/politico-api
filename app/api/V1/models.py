

party_list = []  # empty party list


class PartyModel:
    """This class represents the party model data"""

    def __init__(self, name, hqaddress, logourl):  # constructor
        self.name = name
        self.hqaddress = hqaddress
        self.logourl = logourl

    # this method handles creation of a new party and saving it to party list
    def creating_party(self):
        party_list.append(self)
        return party_list


