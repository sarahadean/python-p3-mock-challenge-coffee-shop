# Deliverables:
# 1. Coffee property name
#       Returns the coffee's name
#       Should not be able to change after the coffee is created
#       hint: hasattr()
#       raise Exception if setter fails
#2. Coffee orders(new_order=None)
#       Adds new orders to coffee
#       Returns a list of all orders for that coffee
#       orders must be of type Order
#       Will be called from Order.__init__
# 3. Coffee customers(new_customer=None)
#       Adds new customers to coffee
#       Returns a unique list of all customers who have ordered a particular coffee.
#       Customers must be of type Customer
#       Will be called from Order.__init__
class Coffee:

    all = []

    def __init__(self, name):
        self.name = name
        self._orders = []
        self._customers = [] #unique list of all customers who have ordered a particular coffee
        Coffee.all.append(self)

    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            raise Exception("Coffee name must be a string")
        
    #returns list of all orders for coffee instance
    def orders(self, new_order=None):
        from classes.order import Order

        if isinstance(new_order, Order):
            self._orders.append(new_order)
        return self._orders
    

    #Returns a unique list of all customers who have ordered a particular coffee.
    def customers(self, new_customer=None):
        from classes.customer import Customer

        if isinstance(new_customer, Customer) and new_customer not in self._customers:
            self._customers.append(new_customer)

        return self._customers
    
    

    def num_orders(self):
        pass
    
    def average_price(self):
        pass