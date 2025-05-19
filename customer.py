from order import Order
class Customer:
    all = []
    def __init__(self,name):
        if len(name) <= 15:
            self._name = name
        else:
            raise TypeError("Name must strictly contain 15 characters and not more!")
        Customer.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,value):
        if len(value) <= 15:
            self.name = value
        elif not isinstance(str,value):
            raise TypeError("Name is not valid")
    def orders(self):
        return [order for order in Order.all if order.customer is self]
    
    def coffees(self):
        return [order.coffee for order in self.orders()]

customer = Customer("Timothy")
