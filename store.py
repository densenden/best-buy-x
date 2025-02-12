class Store:

    def __init__(self):
        self.storage = []

    def remove_product(self, product):
        """Removes a product from store."""
        raise NotImplementedError("This function has not been implemented yet.")

    def get_total_quantity(self):  #-> int
        """Returns how many items are in the store in total."""
        raise NotImplementedError("This function has not been implemented yet.")

    def get_all_products(self): # -> List[Product]
        """Returns all products in the store that are active."""
        raise NotImplementedError("This function has not been implemented yet.")

    def order(self, shopping_list): # -> float
        """Gets a list of tuples, where each tuple has 2 items:
        Product (Product class) and quantity (int).
        Buys the products and returns the total price of the order."""
        raise NotImplementedError("This function has not been implemented yet.")
