from customer import Customer
from coffee import Coffee
# from dataclasses import dataclass
# @dataclass(frozen=True)
class Order:
    def __init__(self,customer,coffee,price):
        self.customer = customer
        self.coffee = coffee
        if  not isinstance(price,float):
            raise ValueError("Price must have 2 decimal places!")
        else:
            self._price = price
        
        Order.customer_orders(self)

    
    @property
    def price(self,price):
        if  not isinstance(price,float):
            raise ValueError("Price must have 2 decimal places")
        elif price >= 100:
            raise ValueError("Price does not exist!")
        else:
            return self._price
    


#customer
order = Order("Adam","Expresso",22.30)
customer = order.customer
print(customer)

#coffee
coffee = order.coffee
print(coffee)
