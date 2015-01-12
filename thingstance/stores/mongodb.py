from ..store import Store
from ..thing import Thing
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError


class MongoStore(Store):

    """MongoDB storage for Things."""

    def __init__(self, client=None,
                 database="thingstance",
                 collection="things"):
        if not client:
            client = MongoClient()
        self.client = client
        self.db = self.client.db[database]
        self.coll = self.db[collection]

    def put(self, thing):
        doc = thing.primitive
        doc['_id'] = thing.hash
        try:
            self.coll.insert(doc)
        except DuplicateKeyError:
            pass

    def get(self, hash):
        doc = self.coll.find_one({'_id': hash})
        del doc['_id']

        thing = Thing()
        thing.primitive = doc
        return thing

store = MongoStore()