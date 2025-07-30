from app import app
from flask import Flask

class EquipmentDataModel:
    def __init__(self, _id, date, aircraft, helicopter, tank, apc, artillery, mrl, auto, fuel_tank, drone, naval_ship, anti_aircraft):
         self.id = _id
         self.date = date
         self.aircraft = aircraft
         self.helicopter = helicopter
         self.tank = tank
         self.apc = apc
         self.artillery = artillery
         self.mrl = mrl
         self.auto = auto
         self.fuel_tank = fuel_tank
         self.drone = drone
         self.naval_ship = naval_ship
         self.anti_aircraft = anti_aircraft
    
    def to_dict(self):
        return {
            "_id":self.id,
            "date": self.date,
            "aircraft": self.aircraft,
            "helicopter": self.helicopter,
            "tank": self.tank,
            "apc": self.apc,
            "artillery": self.artillery,
            "mrl": self.mrl,
            "auto": self.auto,
            "fuel_tank": self.fuel_tank,
            "drone": self.drone,
            "naval_ship": self.naval_ship,
            "anti_aircraft": self.anti_aircraft,
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

class EquipmentData:
    def __init__(self, date, aircraft, helicopter, tank, apc, artillery, mrl, auto, fuel_tank, drone, naval_ship, anti_aircraft):
         self.date = date
         self.aircraft = aircraft
         self.helicopter = helicopter
         self.tank = tank
         self.apc = apc
         self.artillery = artillery
         self.mrl = mrl
         self.auto = auto
         self.fuel_tank = fuel_tank
         self.drone = drone
         self.naval_ship = naval_ship
         self.anti_aircraft = anti_aircraft
    
    def to_dict(self):
        return {
            "date": self.date,
            "aircraft": self.aircraft,
            "helicopter": self.helicopter,
            "tank": self.tank,
            "apc": self.apc,
            "artillery": self.artillery,
            "mrl": self.mrl,
            "auto": self.auto,
            "fuel_tank": self.fuel_tank,
            "drone": self.drone,
            "naval_ship": self.naval_ship,
            "anti_aircraft": self.anti_aircraft,
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