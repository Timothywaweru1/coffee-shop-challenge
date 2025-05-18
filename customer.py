class Customer:
    def __init__(self,name):
        if len(name) <= 15:
            return self._name
        else:
            raise TypeError("Name must strictly contain 15 characters and not more!")

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,value):
        if len(value) <= 15 and isinstance(value,str):
            raise TypeError("Name must contain only 15 characters!")
        else:
            self._name = value