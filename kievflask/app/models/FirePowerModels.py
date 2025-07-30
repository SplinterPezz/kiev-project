from app import app
from flask import Flask

class FirePowerModel:
    def __init__(self, _id, name,  manpower,  financials,  airpower, landPower, navalPower, logistics, resources, geography):
         self.id = _id
         self.name = name
         self.manpower = manpower
         self.financials = financials
         self.airpower = airpower
         self.landPower = landPower
         self.navalPower = navalPower
         self.logistics = logistics
         self.resources = resources
         self.geography = geography
    
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x


class FirePowerData:
    def __init__(self, name,  manpower,  financials,  airpower, landPower, navalPower, logistics, resources, geography):
        self.name = name
        self.manpower = manpower
        self.financials = financials
        self.airpower = airpower
        self.landPower = landPower
        self.navalPower = navalPower
        self.logistics = logistics
        self.resources = resources
        self.geography = geography
    
    def to_dict(self):
        return {
            "name":self.name,
            "manpower": self.manpower,
            "financials": self.financials,
            "airpower": self.airpower,
            "landPower": self.landPower,
            "navalPower": self.navalPower,
            "logistics": self.logistics,
            "resources": self.resources,
            "geography": self.geography
        }