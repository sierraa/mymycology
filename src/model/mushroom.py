
class Mushroom(object):
    """
    A class representing a mushroom
    """

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
