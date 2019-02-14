import json
import unittest
from configs.config import TestingConfig
from app import create_app


app = create_app("testing")


class BaseTest(unittest.TestCase):
    def setUp(self):
        app.config.from_object(TestingConfig)
        self.client = app.test_client()

    def tearDown(self):
        """
          Teardown method runs after every single test
        """
        self.app = None


if __name__ == "__main__":
    unittest.main()
