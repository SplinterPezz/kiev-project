from app import app
from flask import Flask

class OnuDataModel:
    def __init__(self, _id, title, url, download, date, fullDocument, createDate, death=None, injuried=None, deathValues=None):
         self.id = _id
         self.title = title
         self.url = url
         self.download = download
         self.death = death
         self.injuried = injuried
         self.date = date
         self.fullDocument = fullDocument
         self.createDate = createDate
         self.deathValues = deathValues
    
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x


class OnuDataDeathModel:
    def __init__(self, date, death, injuried):
        self.date = date
        self.death = death
        self.injuried = injuried
    
    def to_dict(self):
        return {
            "date": self.date,
            "death": self.death,
            "injuried": self.injuried,
        }

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x