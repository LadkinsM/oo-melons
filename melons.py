from random import choice
from datetime import datetime, time

"""Classes for melon orders."""

class AbstractMelonOrder:
    order_type = None

    def __init__(self, species, qty):
        self.species = species
        self.qty = qty
        self.shipped = False
        self.base_price = 0
        # self.country_code = country_code

        if self.qty > 100: 
            raise TooManyMelonsError("You've ordered too many melons.")

    def get_base_price(self):

        current_day = datetime.now().weekday()
        current_time = datetime.now().time()
        rush_time_start = time(8,0,0,000000)
        rush_time_end = time(11,0,0,000000)

        rush_time = rush_time_start < current_time < rush_time_end

        self.base_price = choice(range(5, 10)) 
       
        if current_day in range(0, 6) and rush_time:
            self.base_price = self.base_price + 4

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

class TooManyMelonsError(ValueError):
    pass
    