from product import Product

class Store(object):
    def __init__(self, products, location, owner):
        self.products = products #an array of products objects
        self.location = location #store address
        self.owner = owner #store owner's name

    def add_product(self, product):
        self.products.append(product)
        return self

    def remove_product(self, prod):
        for product in self.products:
            if product == prod:
                self.products.remove(product)
        return self

    def inventory(self):
        for product in self.products:
            print product.item_name
            print product.price
            print product.weight
            print product.brand
            print product.cost
            print product.status

apples = Product(1, "apples", "10 lb", "a brand", 2)
oranges = Product(2, "oranges", "11 lb", "o brand", 3)
bananas = Product(3, "bananas", "12 lb", "b brand", 2)
watermelons = Product(3, "watermelons", "50 lb", "w brand", 3)

product_list = [apples, oranges, bananas]

wegmans = Store(product_list, "123 Happy Way", "Sadie")
wegmans.remove_product(bananas)
wegmans.inventory()
