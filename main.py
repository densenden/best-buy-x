from colorama import Fore, Style
from products import Product
from store import Store

if __name__ == "__main__":
    print(Fore.YELLOW + "Creating products and store..." + Style.RESET_ALL)
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)
    pixel = Product("Google Pixel 7", price=500, quantity=250)

    best_buy = Store([bose, mac])
    print(Fore.WHITE + f"Initial total quantity in store: {best_buy.get_total_quantity()}" + Style.RESET_ALL)

    print(Fore.YELLOW + "Adding a new product..." + Style.RESET_ALL)
    best_buy.add_product(pixel)
    print(Fore.WHITE + f"Total quantity in store after adding Pixel: {best_buy.get_total_quantity()}" + Style.RESET_ALL)

    print(Fore.YELLOW + "Removing a product..." + Style.RESET_ALL)
    best_buy.remove_product(mac)
    print(Fore.WHITE + f"Total quantity in store after removing Mac: {best_buy.get_total_quantity()}" + Style.RESET_ALL)

    print(Fore.YELLOW + "Placing an order for 2 Bose Earbuds and 5 Google Pixels..." + Style.RESET_ALL)
    order_cost = best_buy.order([(bose, 2), (pixel, 5)])
    print(Fore.WHITE + f"Total order cost: {order_cost}" + Style.RESET_ALL)

    print(Fore.YELLOW + "Checking active products..." + Style.RESET_ALL)
    active_products = best_buy.get_all_products()
    for product in active_products:
        print(Fore.WHITE + f"- {product.name}: {product.quantity} available" + Style.RESET_ALL)

    print(Fore.YELLOW + "Final total quantity in store:" + Style.RESET_ALL)
    print(Fore.WHITE + f"{best_buy.get_total_quantity()}" + Style.RESET_ALL)
