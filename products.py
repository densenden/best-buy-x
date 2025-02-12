class Product:

    def __init__(self, name, price, quantity):
        if not name:
            raise ValueError("Enter a name. This can't be empty.")

        if price < 0:
            raise ValueError("Price cannot be negative.")

        if quantity < 0:
            raise ValueError("Quantity Error: What were you thinking?")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self):  # -> float
        return self.quantity

    def set_quantity(self, quantity):
        if quantity < 0:
            raise ValueError("We cannot handle negative stock.")

        self.quantity = quantity

        self.active = quantity > 0

    def is_active(self):
        return self.active

    def activate(self):
        raise NotImplementedError(f"note by densenden:\nfunction not implemented yet")

    def deactivate(self):
        raise NotImplementedError(f"note by densenden:\nfunction not implemented yet")

    def show(self):  # -> str
        raise NotImplementedError(f"note by densenden:\nfunction not implemented yet")

    def buy(self, quantity): # -> float
        raise NotImplementedError(f"note by densenden:\nfunction not implemented yet")

