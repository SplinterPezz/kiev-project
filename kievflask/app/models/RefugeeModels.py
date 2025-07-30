from app import app
from flask import Flask

class RefugeeAggregatedModel:
    def __init__(self, _id, value, nation):
         self.id = _id
         self.value = value
         self.nation = nation
    
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x


class RefugeeAggregatedDataModel:
    def __init__(self, value, nation):
        self.value = value
        self.nation = nation
    
    def to_dict(self):
        return {
            "value": self.value,
            "nation": self.nation,
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
        
class RefugeeDailyModel:
    def __init__(self, _id, date, value):
         self.id = _id
         self.date = date
         self.value = value
    
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x


class RefugeeDailyDataModel:
    def __init__(self, date, value):
        self.date = date
        self.value = value
    
    def to_dict(self):
        return {
            "date": self.date,
            "value": self.value,
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