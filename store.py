class Store:
    storage = []

    def __init__(self)


    def remove_product(self, product):
    """Removes a product from store."""


    def get_total_quantity(self):  #-> int
    """Returns how many items are in the store in total."""

    def get_all_products(self): # -> List[Product]
    """Returns all products in the store that are active."""

    def order(self, shopping_list): # -> float
    """Gets a list of tuples, where each tuple has 2 items:
    Product (Product class) and quantity (int).
    Buys the products and returns the total price of the order."""

