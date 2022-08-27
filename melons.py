"""Classes for melon orders."""
class AbstractMelonOrder:
    order_type = None

    def __init__(self, species, qty, country_code = None):
        self.species = species
        self.qty = qty
        self.shipped = False
        self.country_code = country_code

    def get_total(self):
        """Calculate price, including tax."""
        total = 0

        base_price = 5

        if self.species == 'Christmas Melon':
            total = (1 + self.tax) * self.qty * (base_price * 1.5)
        else: 
            total = (1 + self.tax) * self.qty * base_price

        if self.qty < 10 and self.country_code != None:
            total = total + 3

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

    def get_country_code(self):
        """Return the country code."""

        return self.country_code


# (self, species, qty, country_code = None):