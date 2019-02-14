import sys
import json
from .base_test import BaseTest

sys.path.append("app")
from utils.dummy_data.office_dummy_data import office_1


class TestOfficeModel(BaseTest):
    """method is used will be used to construct all our test"""

    #  test case for creating a office
    def test_post_office(self):
        response = self.client.post('/api/v1/offices', data=json.dumps(office_1),
                                    content_type="application/json")
        posted_office = json.loads(response.data.decode('utf-8'))  # response decoding
        self.assertEqual(response.status_code, 201)
        self.assertEqual(posted_office["status"], 201)
        self.assertEqual(posted_office["data"][0]["type"], "National")
        self.assertEqual(posted_office["data"][0]["name"], "Office of the President")

    def test_get_all_offices(self):
        response_data = self.client.get(path='/api/v1/offices', content_type='application/json')
        self.assertEqual(response_data.status_code, 200)

    def test_get_single_office(self): # test the validity of the get method
        response = self.client.get(path='/api/v1/offices', content_type="application/json")
        requested_office = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(requested_office["status"], 200)

