from app import app
from flask import Flask

class KievArticleModel:
    def __init__(self, _id, title, date, main, tag=None, customTag=None, deaths=None):
         self.id = _id
         self.title = title
         self.date = date
         self.main = main
         self.tag = tag
         self.customTag = customTag
         self.deaths = deaths
    
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x


class KievArticleTagModel:
    def __init__(self, date, tags):
        self.date = date
        self.tags = tags
    
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x


class KievArticleDeathModel:
    def __init__(self, date, death):
        self.date = date
        self.death = death
    
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x