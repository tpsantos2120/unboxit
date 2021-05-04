import unittest
from unboxit import app
from unboxit.models.db import db


class BaseCase(unittest.TestCase):

    """
        Construct the app and db instances
    """
    def setUp(self):
        self.app = app.test_client()
        self.db = db.get_db()

    """
        Once test is completed delete entries from db
    """
    def tearDown(self):
        for collection in self.db.list_collection_names():
            self.db.drop_collection(collection)