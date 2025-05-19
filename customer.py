class Customer:
    def __init__(self,name):
        if len(name) <= 15:
            self._name = name
        else:
            raise TypeError("Name must strictly contain 15 characters and not more!")

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,value):
        if len(value) <= 15:
            self.name = value
        elif not isinstance(str,value):
            raise TypeError("Name is not valid")