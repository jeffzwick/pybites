from datetime import datetime

NOW = datetime.now()


class Promo:
    def __init__(self, name, expires):
        self.name = name
        self.expires = expires

    @property
    def expired(self):
        return NOW > self.expires

"""
Write a simple Promo class. Its constructor receives a name str and expires datetime.
Add a property called expired which returns a boolean value indicating whether the promo has expired or not.
"""