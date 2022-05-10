class Basket:
    def __init__(self, productName=None, productPrice=None):
        self.productName = productName  # Название товара
        self.productPrice = productPrice  # Цена товара
        self.total = None


#    def basketSum(self):
 #       self.total = sum(self.productPrice)