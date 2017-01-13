"""This file should have our order classes in it."""


class AbstactMelonOrder(object):
    shipped = False

    def __init__(self, species, qty, order_type=None, tax=None):
        self.species = species
        self.qty = qty
        if order_type:
            self.order_type = order_type
        if tax:
            self.tax = tax

    def get_total(self):
        """Calculate price."""
        base_price = 5
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
        super(InternationalMelonOrder, self).__init__(species, qty,
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
