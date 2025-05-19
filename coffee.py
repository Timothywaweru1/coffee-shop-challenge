
class Coffee:
    def __init__(self,name):
        if len(name) >= 3 and isinstance(name,str):
            return self._name
        else:
            raise TypeError("Coffee must contain 3 characters or more!")
    
    @property
    def name(self):
        return self._name
    
    