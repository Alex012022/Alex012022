'''
Модуль для работы с товарами
'''

class Product:
    def __init__(self, productName=str, productPrice=float, productRating=int):
        self.productName = productName      #Название товара
        self.productPrice = productPrice    #Цена товара
        self.productRating = productRating  #Рейтинг товара

    def printing_product_data(pr):
        if not isinstance(pr, Product):
            raise TypeError("Это не товар")
        print(f'Название товара: {pr.productName}')
        print('Цена товара:')
        print(' ' * 2, pr.productPrice)
        print(f'Рейтинг товара:', pr.productRating)


