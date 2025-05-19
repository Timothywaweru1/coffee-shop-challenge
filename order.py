
class Order:
    all = []
    def __init__(self,customer,coffee,price):
        self._customer = customer
        self._coffee = coffee
        if  not isinstance(price,float):
            raise ValueError("Price must have 2 decimal places!")
        else:
            self._price = price
        Order.all.append(self)
        
    @property
    def price(self,price):
        if  not isinstance(price,float):
            raise ValueError("Price must have 2 decimal places")
        elif price >= 100:
            raise ValueError("Price does not exist!")
        else:
            return self._price
    
    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee
    


#customer
order = Order("Adam","Expresso",22.30)
customer = order.customer
print(customer)

#coffee
coffee = order.coffee
print(coffee)
