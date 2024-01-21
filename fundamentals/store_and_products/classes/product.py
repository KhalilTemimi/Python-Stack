

class Product():
    count = 0
    def __init__(self,name, price, category):
        self.id = Product.count
        Product.count +=1
        self.name = name
        self.price = price
        self.category = category

    def update_price(self,percent_change,is_increased):
        if Product.is_increased(is_increased):
            self.price += (percent_change*self.price)
        else:
            self.price -= (percent_change*self.price)
        return self
    
    def get_category(self):
        return self.category

    def products_info(self):
        print(f"Id: {self.id}, Product Name: {self.name}, Price: {self.price}, Category: {self.category}")
        return self

    @staticmethod
    def is_increased(is_increased):
        if(is_increased == "up"):
            return True
        elif(is_increased == "down"):
            return False