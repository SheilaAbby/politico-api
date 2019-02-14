
import json
import unittest
from app import current_app
from app.api.V1 import models


class TestPartyModel(unittest.TestCase):
    """method is used will be used to construct all our test"""
    def setUp(self):  # acts as a constructor for the tests
        self.app = app
        self.client = self.app.test_client()  # test client inbuilt  to run our tests
        self.data = {  # party data
                "id": 1,
                "name": "jubilee",
                "hqaddress": "hqaddress",
                "logoUrl": "localhost"
        }
        self.da = { 
                "id": 1,
                "name": "jubilee",
                "hqaddress": "hqaddress",
                "logoUrl": "localhost"
            }

    #  test case for creating a party
    def test_post_party(self):
        response_data = self.client.post('/parties/', data=json.dumps(self.data),
                                         headers={'Content-Type': 'application/json'})
        self.assertEqual(response_data.status_code, 201)
        self.assertEqual(response_data.get_json['status'], 201)
        self.assertEqual(response_data.get_json['message'], 'party created')

    def test_get_all_parties(self):
        response_data = self.client.get(path='/parties', content_type='application/json')
        self.assertEqual(response_data.status_code, 200)

    def test_get_single_political_party(self):
        party = self.client.post(path='/parties', data=json.dumps(self.data), content_type="application/json")
        int_id = int(party.get_json('id'))
        path = '/parties/1'
        response_data = self.client.get(path, content_type="application/json")
        self.assertEqual(response_data.status_code, 200)

    def test_edit_political_party(self):
        party = self.client.post(path='/parties', data=json.dumps(self.data), content_type="application/json")
        int_id = int(party.get_json('id'))
        path = '/parties/{}/{}'.format(int_id)
        response_data = self.client.patch(path, data=json.dumps(self.da), content_type='application/json')
        self.assertEqual(response_data.status_code, 200)

    def test_delete_political_party(self):
        party = self.client.post(path='/parties', data=json.dumps(self.data), content_type='application/json')
        int_id = int(party.get_json('id'))
        path = '/parties/{}'.format(int_id)
        response_data = self.client.delete(path, content_type='application/json')
        self.assertEqual(response_data.status_code, 200)


if __name__ == '__main__':
    unittest.main()
