"""This file should have our order classes in it."""
from random import randint
from datetime import datetime


class AbstactMelonOrder(object):
    shipped = False

    def __init__(self, species, qty, order_type=None, tax=None):
        self.species = species
        self.qty = qty
        if order_type:
            self.order_type = order_type
        if tax:
            self.tax = tax

    def get_base_price(self):
        cur_moment = datetime.now()
        # get number of day in week (1 - Monday, 2 - Tuesday...)
        weekday = cur_moment.isoweekday()
        # get hour
        hour = cur_moment.hour
        # create random base price
        base_price = randint(5, 9)
        print " random price: ", base_price
        # from 8am-11am and Mon-Fri add extra $4
        if weekday in range(1, 6) and (hour >= 8 and hour < 11):
            base_price += 4
        print "final price: ", base_price
        return base_price

    def get_total(self):
        """Calculate price."""
        base_price = self.get_base_price()
        if self.species == "Christmas melon":
            base_price = 1.5*base_price
        total = (1 + self.tax) * self.qty * base_price
        return total

    def mark_shipped(self):
        """Set shipped to true."""
        self.shipped = True


class DomesticMelonOrder(AbstactMelonOrder):
    """A domestic (in the US) melon order."""
    order_type = "domestic"
    tax = 0.08


class InternationalMelonOrder(AbstactMelonOrder):
    """An international (non-US) melon order."""
    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""
        super(InternationalMelonOrder, self).__init__(species,
                                                      qty,
                                                      order_type="international",
                                                      tax=0.17)
        self.country_code = country_code

    def get_total(self):
        """Calculate price."""
        total = super(InternationalMelonOrder, self).get_total()
        if self.qty < 10:
            total += 3
        return total

    def get_country_code(self):
        """Return the country code."""
        return self.country_code


class GovernmentMelonOrder(AbstactMelonOrder):
    tax = 0
    order_type = 'government'
    passed_inspection = False

    def mark_inspection(self, passed):
        self.passed_inspection = passed
