
import re

from utils.Password import check_buyer
from utils.category import Category
from utils.Product import Product
from utils.Basket import Basket


check_buyer()

ch = 'y'

while ch == 'y':
    category1 = Category(1, 'Мелкая бытовая техника')
    category2 = Category(2, 'Крупная бытовая техника')
    category3 = Category(3, 'Техника для дома')
    category4 = Category(4, 'Красота и здоровье')

    print('Выберете категорию')
    print(category1.categoryNum, '-', category1.categoryName)
    print(category2.categoryNum, '-', category2.categoryName)
    print(category3.categoryNum, '-', category3.categoryName)
    print(category4.categoryNum, '-', category4.categoryName)

    selectedCategory = int(input('выбранная категория: '))
    if selectedCategory == category1.categoryNum:
        print(category1.categoryNum)
        cat_Name = category1.categoryName
        print('Выбрана категория: ', cat_Name)
        print('Выберите товар')
    elif selectedCategory == category2.categoryNum:
        cat_Name = category2.categoryName
        print('Выбрана категория: ', cat_Name)
        print('Выберите товар')
    elif selectedCategory == category3.categoryNum:
        cat_Name = category3.categoryName
        print('Выбрана категория: ', cat_Name)
        print('Выберите товар')
    else:
        cat_Name = category4.categoryName
        print('Выбрана категория: ', cat_Name)
        print('Выберите товар')

    i = 1
    product_dic = {}  # создаем пустой словарь
    with open("list.txt", encoding="utf-8") as f:
        for line in f:
            if line.split(",")[0] == cat_Name:
                product_srt = Product(line.split(",")[1], line.split(",")[2], line.split(",")[3])
                product_dic[i] = product_srt.productName, product_srt.productPrice   # в цикле заполняем словарь названием товара
                print(i, 'Название товара: ', product_srt.productName)
                print(' ' * 4, 'Цена: ', product_srt.productPrice)
                print(' ' * 4, 'Рейтинг товара', product_srt.productRating)
                i += 1       # подсчет количества строк

#   print('Словарь', product_dic)

    selectedProduct = int(input('выбранный товар: '))
    if selectedProduct in product_dic:
        #print(selectedProduct, product_dic[selectedProduct])
        basket1 = Basket(product_dic[selectedProduct])
        print('В корзину добавлен товар: ', basket1.productName)

        fp = open('Basket.txt', "a", encoding="utf-8")  # открыть файл для записи с сохранением существующих записей (а- добавление записи в конец списка)
        fp.write(str(basket1.productName) + '\n')
        fp.close()
    #print('Товар добавлен в корзину')

    ch = input('Продолжить покупки (y/n)? ')

    f4 = 0
    i = 0
    if ch == 'n':
        with open("Basket.txt", encoding="utf-8") as f1:
            for line in f1:
                f2 = re.sub("[(|'|)]", "", line)
                f3 = int(f2.rpartition(' ')[-1])
                f4 = f4 + f3
                i += 1
               # print(f3)
            print('В корзине', i, 'шт. товара на сумму:', f4)

