
import json
from tests.base_test import BaseTest
from utils.dummy_data.party_dummy_data import party_1, party_to_edit, party_to_delete


class TestPartyModel(BaseTest):
    """method is used will be used to construct all our test"""

    #  test case for creating a party
    def test_post_party(self):
        response = self.client.post('/api/v1/parties', data=json.dumps(party_1),
                                    content_type="application/json")
        posted_party = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 201)
        self.assertEqual(posted_party["status"], 201)
        self.assertEqual(posted_party["data"][0]["logoUrl"], "localhost")

    def test_get_all_parties(self):
        response_data = self.client.get(path='/api/v1/parties', content_type='application/json')
        parties = json.loads(response_data.data.decode('utf-8'))
        self.assertEqual(response_data.status_code, 200)
        # check the 200 ok status after successful fetching
        self.assertEqual(parties["status"], 200)

    def test_get_single_political_party(self):
        response = self.client.get("/api/v1/parties/1", content_type="application/json")
        single_party = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(single_party["status"], 200)
        self.assertEqual(single_party["data"][0]["id"], 1)

    def test_edit_political_party(self):
        response = self.client.get(path='/api/v1/parties/1/name', data=json.dumps(party_to_edit), content_type="application/json")
        party = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(party["status"], 200)
        self.assertEqual(party["data"][0]["message"], "successfully updated name")

    def test_delete_political_party(self):
        response = self.client.delete(
            "/api/v1/parties/2", content_type="application/json")
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["data"][0]["message"], "delete successful")


