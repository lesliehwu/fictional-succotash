class Product(object):
    def __init__(self,price,item_name,weight,brand,cost):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = "for sale"

    def sell(self):
        self.status = "sold"

        return self

    def add_tax(self,tax):
        self.price *= (1 + tax)
        self.price = round(self.price,2)

        return self

    def return_me(self,why_are_you_like_this):
        self.status = why_are_you_like_this
        if(why_are_you_like_this == "defective"):
            self.price = 0
        elif(why_are_you_like_this == "like new"):
            self.status = "for sale"
        elif(why_are_you_like_this == "opened"):
            self.status = "used"
            self.price *= 0.8

        return self
        

    def display_info(self):
        print("Price:",self.price)
        print("Item Name:",self.item_name)
        print("Weight:",self.weight)
        print("Brand:",self.brand)
        print("Cost:",self.cost)
        print("Status:",self.status)

oranges = Product(3,"oranges","500lb","Sunkist",2)
oranges.sell().display_info()
oranges.add_tax(0.13).display_info()
oranges.return_me("defective").display_info()
