#intermediary
#Deliverables:
# 1. Order __init__(self, customer, coffee, price)
#       Orders should be initialized with a customer, coffee, and a price (a number)
# 2. Order property price
#       Returns the price for a coffee
#       Price must be a number between 1 and 10, inclusive
#       raise Exception if setter fails
# 3. Order property customer
#       Returns the customer object for that order
#       Must be of type Customer
#       raise Exception if setter fails
# 4. Order property coffee
#       Returns the coffee object for that order
#       Must be of type Coffee
#       raise Exception if setter fails

class Order:
    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

        coffee.orders(self)
        coffee.customers(customer)
        customer.orders(self)
        customer.coffees(coffee)
        

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        if isinstance(price, int) and 1 <= price <= 10:
            self._price = price
        else:
            raise Exception("Price must be number between 1 and 10")
        
    #checking if customer instance exists
    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, customer):
        from classes.customer import Customer
        if isinstance(customer, Customer):
            self._customer = customer
        else:
            raise Exception('Customer instance does not exist')
        
    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, coffee):
        from classes.coffee import Coffee
        if isinstance(coffee, Coffee):
            self._coffee = coffee
        else:
            raise Exception('Coffee instance does not exist')
