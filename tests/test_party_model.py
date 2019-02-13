import sys
import json
import unittest
from run import app

sys.path.append("app")

from app import *


class TestParty(unittest.TestCase):
    """method is used will be used to construct all our test"""
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        self.data = {  # party data
                "id":1,
                "name": "jubilee",
                "hqaddress": "hqaddress",
                "logoUrl": "localhost"
        }
        self.da = { 
                "id":1,
                "name": "jubilee",
                "hqaddress": "hqaddress",
                "logoUrl": "localhost"
            }

    #  test case for creating a party
    def test_creating_party(self):
        response_data = self.client.post('/parties/', data=json.dumps(self.data),
                                         headers={'Content-Type': 'application/json'})
        self.assertEqual(response_data.status_code, 201)
        self.assertIn(1, int(response_data.data))
        self.assertIn('jubilee', str(response_data.data)) # check value to be a string
        self.assertIn('localhost', str(response_data.data))
        self.assertEqual(response_data.get_json['status'], 201)

    def test_getting_all_parties(self):
        response_data = self.client.get(path='/parties', content_type='application/json')
        self.assertEqual(response_data.status_code, 200)

    def test_getting_single_party(self):
        party = self.client.post(path='/parties', data=json.dumps(self.data), content_type="application/json")
        id = int(party.get_json('id'))
        path = '/parties/{}'.format(id)
        response_data = self.client.get(path, content_type="application/json")
        self.assertEqual(response_data.status_code, 200)

    def test_editing_a_party(self):
        party = self.client.post(path='/parties', data=json.dumps(self.data), content_type="application/json")
        id = int(party.get_json('id'))
        name = party.get_json('name')
        path = '/parties/{}/{}'.format(id, name)
        response_data = self.client.patch(path, data=json.dump(self.da), content_type='application/json')
        self.assertEqual(response_data.status_code, 200)

    def test_deleting_a_party(self):
        party = self.client.post(path='/parties', data=json.dumps(self.data), content_type='application/json')
        id = int(party.get_json('id'))
        path = '/parties/{}'.format(id)
        response_data = self.client.delete(path, content_type='application/json')
        self.assertEqual(response_data.status_code, 200)


if __name__ == '__main__':
    unittest.main()
