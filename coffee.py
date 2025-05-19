from order import Order
class Coffee:
    def __init__(self,name):
        if len(name) >= 3 and isinstance(name,str):
            return self._name
        else:
            raise TypeError("Coffee must contain 3 characters or more!")
    
    @property
    def name(self):
        return self._name
    
    def orders(self):
        return [order for order in Order.all if order.coffee is self]
    
    def customer(self):
        return [order.customer for order in self.orders()]
    
    def average_price(self):
        prices = [order.price for order in self.orders()]
        if not prices:
            return 0
        else:
            return sum(prices) / len(prices)


    