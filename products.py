class Product:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self):  # -> float
        raise NotImplementedError(f"note by densenden:\nfunction not implemented yet")

    def set_quantity(self, quantity):
        raise NotImplementedError(f"note by densenden:\nfunction not implemented yet")

    def is_active(self):  # -> bool
        raise NotImplementedError(f"note by densenden:\nfunction not implemented yet")

    def activate(self):
        raise NotImplementedError(f"note by densenden:\nfunction not implemented yet")

    def deactivate(self):
        raise NotImplementedError(f"note by densenden:\nfunction not implemented yet")

    def show(self):  # -> str
        raise NotImplementedError(f"note by densenden:\nfunction not implemented yet")

    def buy(self, quantity): # -> float
        raise NotImplementedError(f"note by densenden:\nfunction not implemented yet")

