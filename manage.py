from product import Product
from store import Store


tampons = Product(3.5, "tampons", "1 lb", "always", 2.2)
deedle = Product(2.1, "cheetoes","12 lb", "frito-lay", 300.5)
doodle = Product(5.4, "donuts","41 lb", "krispy", 32.54)
products = [tampons, deedle, doodle]
safeway = Store(products, "135 Blueberry Lane", "me")
safeway.inventory()
