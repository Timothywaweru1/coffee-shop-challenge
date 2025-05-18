from customer import Customer
from coffee import Coffee
from dataclasses import dataclass
@dataclass(frozen=True)
class Order:
    def __init__(self,customer,coffee,price):
        self.customer = customer
        self.coffee = coffee
        if  not isinstance(price,float):
            raise ValueError("Price must have 2 decimal places!")
        else:
            self.price = price
    
    @property
    def price(self,price):
        if  not isinstance(price,float):
            raise ValueError("Price must have 2 decimal places")
        elif price >= 100:
            raise ValueError("Price does not exist!")
        else:
            return self._price

