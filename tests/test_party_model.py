
import json
import unittest
from app import current_app
from app import create_app
from app.api.V1 import models
from utils.dummy_data.party_dummy_data import party_1


class TestPartyModel(unittest.TestCase):
    """method is used will be used to construct all our test"""
    def setUp(self):  # acts as a constructor for the tests
        self.app = create_app()
        self.client = self.app.test_client()  # test client inbuilt  to run our tests

    #  test case for creating a party
    def test_post_party(self):
        response = self.client.post('/api/v1/parties', data=json.dumps(party_1),
                                    content_type="application/json")
        posted_party = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 201)
        self.assertEqual(posted_party["status"], 201)
        self.assertEqual(posted_party["data"][0]["name"], "jubilee")
        self.assertEqual(posted_party["data"][0]["logoUrl"], "localhost")
        self.assertEqual(posted_party["data"][0]["hqAddress"], "PO BOX 445 NB")

    def test_get_all_parties(self):
        response_data = self.client.get(path='/api/v1/parties', content_type='application/json')
        self.assertEqual(response_data.status_code, 200)

    def test_get_single_political_party(self):
        response = self.client.get("/api/v1/parties/1", content_type="application/json")
        single_party = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(single_party["status"], 200)
        self.assertEqual(single_party["data"][0]["id"], 1)

    def test_edit_political_party(self):
        party = self.client.post(path='/api/v1/parties', data=json.dumps(self.data), content_type="application/json")
        int_id = int(party.json['id'])
        path = '/parties/{}/{}'.format(int_id)
        response_data = self.client.patch(path, data=json.dumps(self.da), content_type='application/json')
        self.assertEqual(response_data.status_code, 200)

    def test_delete_political_party(self):
        party = self.client.post(path='/api/v1/parties', data=json.dumps(self.data), content_type='application/json')
        int_id = int(party.json['id'])
        path = '/parties/{}'.format(int_id)
        response_data = self.client.delete(path, content_type='application/json')
        self.assertEqual(response_data.status_code, 200)


if __name__ == '__main__':
    unittest.main()
