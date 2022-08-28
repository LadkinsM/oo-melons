from random import choice
from datetime import datetime

"""Classes for melon orders."""

class AbstractMelonOrder:
    order_type = None

    def __init__(self, species, qty):
        self.species = species
        self.qty = qty
        self.shipped = False
        self.base_price = 0
        # self.country_code = country_code

    def get_base_price(self):

        current_day = datetime.now().weekday()
        current_time = datetime.now().time()
        # no = today_day.weekday()

        print(type(current_day))
        print(type(current_time))

        if current_day in range(0, 6) and current_time in range(8, 8):
            print("Date is Weekday")
        # else:  

        self.base_price = choice(range(5, 10))

        return self.base_price

    def get_total(self):
        """Calculate price, including tax."""
        
        total = 0

        if self.species == 'Christmas Melon':
            total = (1 + self.tax) * self.qty * (self.get_base_price() * 1.5)
        else: 
            total = (1 + self.tax) * self.qty * self.get_base_price()

        # if self.qty < 10 and self.country_code != None:
        #     total = total + 3

        return total
    
    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True



    
class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    order_type = "domestic"
    tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17

    def __init__(self, species, qty, country_code):
        
        self.country_code = country_code

        super().__init__(species, qty)

    
    def get_total(self):
        
        total = super().get_total()

        if self.qty < 10:
            total = total + 3

        return total


    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):

    order_type = 'government'
    tax = 0.00
    passed_inspection = False

    def mark_inspection(self, passed):
        """Records that inspection has been passed"""

        passed_inspection = True


# (self, species, qty, country_code = None):


# >>> class Polygon(object):
# ...     def __init__(self, id):
# ...         self.id = id
# ...
# >>> class Rectangle(Polygon):
# ...     def __init__(self, id, width, height):
# ...         super(self.__class__, self).__init__(id)
# ...         self.shape = (width, height)