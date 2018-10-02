from google.cloud import datastore

class MushroomMapper(object):

    def __init__(self):
        self.client = datastore.Client()

    def put_mushroom(self, mushroom):
        self.client.put(mushroom)
