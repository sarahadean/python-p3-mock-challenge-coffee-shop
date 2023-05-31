# Deliverables:
# 1. Customer property name:
#       Return name
#       Names must be of type str
#       Names must be between 1 and 15 characters, inclusive
#       raise Exception if setter fails

class Customer:
    all = []

    def __init__(self, name):
        self.name = name
        self._orders = []
        self._coffees = []
        Customer.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise Exception('Name must be string between 1 and 15 characters')
        

    def orders(self, new_order=None):
        from classes.order import Order

        if isinstance(new_order, Order):
            self._orders.append(new_order)
        return self._orders
    

    def coffees(self, new_coffee=None):
        from classes.coffee import Coffee

        if isinstance(new_coffee, Coffee) and new_coffee not in self._coffees:
            self._coffees.append(new_coffee)
        return self._coffees
    
    def create_order(coffee, price):
        return Customer(coffee, price)
        # self._orders.append()
    
#     Customer
# Customer create_order(coffee, price)
# given a coffee object and a price(as an integer), creates a new order and associates it with that customer and coffee.