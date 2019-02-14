import sys
import json
import unittest
from app import create_app
sys.path.append("app")
from utils.dummy_data.office_dummy_data import office_1


class TestOfficeModel(unittest.TestCase):
    """method is used will be used to construct all our test"""
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    #  test case for creating a office
    def test_post_office(self):
        response = self.client.post('/api/v1/offices', data=json.dumps(office_1),
                                    content_type="application/json")
        posted_office = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 201)
        self.assertEqual(posted_office["status"], 201)
        self.assertEqual(posted_office["data"][0]["name"], "jubilee")
        self.assertEqual(posted_office["data"][0]["logoUrl"], "localhost")

    def test_get_all_offices(self):
        response_data = self.client.get(path='/api/v1/offices', content_type='application/json')
        self.assertEqual(response_data.status_code, 200)

    def test_get_single_office(self): # test the validity of the get method
        response = self.client.get(path='/api/v1/offices', content_type="application/json")
        requested_office = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(requested_office["status"], 200)


if __name__ == '__main__':
    unittest.main()
