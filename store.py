class Store:

    def __init__(self, products=None):
        """Initializes the store with an optional list of products."""
        self.storage = products if products is not None else []

    def add_product(self, product):
        """Adds a new product or increases quantity if it already exists."""
        for existing_product in self.storage:
            if existing_product.name == product.name:
                existing_product.quantity += product.quantity
                return
        self.storage.append(product)

    def remove_product(self, product):
        """Removes a product from store."""
        if product in self.storage:
            self.storage.remove(product)
        else:
            raise ValueError(f"Product '{product.name}' not found in store.")

    def get_total_quantity(self):  #-> int
        """Returns how many items are in the store in total."""
        return sum(product.quantity for product in self.storage)

    def get_all_products(self): # -> List[Product]
        """Returns all products in the store that are active."""
        return [product for product in self.storage if product.is_active()]

    def order(self, shopping_list): # -> float
        """Gets a list of tuples, where each tuple has 2 items:
        Product (Product class) and quantity (int).
        Buys the products and returns the total price of the order."""
        total_price = 0
        for product, quantity in shopping_list:
            if product in self.storage and product.get_quantity() >= quantity:
                total_price += product.price * quantity
                product.set_quantity(product.get_quantity() - quantity)
            else:
                raise ValueError(f"Not enough stock for {product.name}")
        return total_price
