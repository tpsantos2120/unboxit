import unittest
from unboxit import app
from unboxit.models.db import db


class BaseCase(unittest.TestCase):
    """
        Abstract the use of the methods below so ti does
        not have to repeat in every file test.
    """

    def setUp(self):
        """
            Construct the app and db instances.
        """
        self.app = app.test_client()
        self.db = db.get_db()

    def tearDown(self):
        """
            Once test is completed delete collections from db.
        """
        for collection in self.db.list_collection_names():
            self.db.drop_collection(collection)
