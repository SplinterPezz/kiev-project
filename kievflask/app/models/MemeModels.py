class MemeMongoModel:
    def __init__(self, _id, date, name, text, source):
         self.id = _id
         self.date = date
         self.name = name
         self.text = text
         self.source = source
    
    def to_dict(self):
        return {
            "_id":self.id,
            "date": self.date,
            "name": self.name,
            "text": self.text,
            "source":self.source
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
    
class MemeModel:
    def __init__(self, date, name, text, source):
         self.date = date
         self.name = name
         self.text = text
         self.source = source
    
    def to_dict(self):
        return {
            "date": self.date,
            "name": self.name,
            "text": self.text,
            "source":self.source
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