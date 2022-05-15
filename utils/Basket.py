import re
'''
Модуль для работы с товарами в корзине
'''
class Basket:
    def __init__(self, productName=None, productPrice=None):
        self.productName = productName  # Название товара
        self.productPrice = productPrice  # Цена товара

    '''
    Функция суммирования стоимости товара
    '''
    def basketSum():
        file4 = 0
        i = 0
        with open("Basket.txt", encoding="utf-8") as file1:
            for line in file1:
                file2 = re.sub("[(|'|)]", "", line)
                file3 = int(file2.rpartition(' ')[-1])
                file4 += file3
                i += 1
            print(f'В корзине  {i} шт. товара на сумму: {file4}')