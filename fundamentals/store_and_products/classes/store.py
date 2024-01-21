from classes.product import Product

class Store():
    def __init__(self,name):
        self.name = name
        self.products = []

    def add_product(self,product):
        self.products.append(product)
        return self

    def sell_product(self,id):
        for i, product in enumerate (self.products):
            if product.id == id:
                self.products.remove(self.products[i])
        return self

    def store_info(self):
        print(f"\nShop Name: {self.name}, List of Products:\n")
        for i in range (len(self.products)):
            Product.products_info(self.products[i])
        return self
    
    def inflation(self,percent_increase):
        for i in range(len(self.products)):
            self.products[i].update_price(percent_increase,is_increased="up")
        return self
        # for i in self.products:
        #     i.uupdate_price(percent_increase,is_increased="up")

    def set_clearance(self, category, percent_discount):
        for i in range (len(self.products)):
            if (self.products[i].get_category() == category):
                self.products[i].update_price(percent_discount,is_increased="down")
        return self