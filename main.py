from utils.Password import check_buyer
from utils.category import Category
from utils.Product import Product
from utils.Basket import Basket

'''
Проверка логина и пароль пользователя
ch: Переменная продолжения совершения покупок (значения y/n)
selectedCategory: переменная содержащая номер выбранной категории
cat_Name: переменная содержащая наименование выбранной категории
selectedProduct: переменная содержащая номер выбранног товара

'''
check_buyer()

ch = 'y'

while ch == 'y':

    '''
    Вывод списка категории товара
    '''
    Category.checkCategory()

    selectedCategory = int(input('выбранная категория: '))

    '''
    Проверка существования номера категории
    '''
    while (selectedCategory not in [1,2,3,4]):
        print('Выбранной категории не существует')
        selectedCategory = int(input('Выберите категорию: '))

    '''
    Отображение наименований выбранной категории
    '''
    if selectedCategory == 1:
        cat_Name = Category(categoryName='Мелкая бытовая техника')
        print(cat_Name.categoryName)
    elif selectedCategory == 2:
        cat_Name = Category(categoryName='Крупная бытовая техника')
        print(cat_Name.categoryName)
    elif selectedCategory == 3:
        cat_Name = Category(categoryName='Техника для дома')
        print(cat_Name.categoryName)
    elif selectedCategory == 4:
        cat_Name = Category(categoryName='Красота и здоровьеа')
        print(cat_Name.categoryName)
    else:
        print('Указанной категории не существует')

    '''
    Вывод списка товара из указанной категории
    '''
    i = 1
    product_dic = {}  # создаем пустой словарь
    with open("list.txt", encoding="utf-8") as f:
        for line in f:
            if line.split(",")[0] == cat_Name.categoryName:
                product_srt = Product(line.split(",")[1], line.split(",")[2], line.split(",")[3])
                product_dic[i] = product_srt.productName, product_srt.productPrice   # в цикле заполняем словарь названием товара
                print(i, 'Название товара: ', product_srt.productName)
                print(' ' * 4, 'Цена: ', product_srt.productPrice)
                print(' ' * 4, 'Рейтинг товара', product_srt.productRating)
                i += 1       # подсчет количества строк


    '''
    Отображение добавленного в корзину товара
    '''
    selectedProduct = int(input('выбранный товар: '))
    if selectedProduct in product_dic:
        #print(selectedProduct, product_dic[selectedProduct])
        basket1 = Basket(product_dic[selectedProduct])
        print('В корзину добавлен товар: ', basket1.productName)

        '''
        Запись данных о добавленном товаре в файл 'Basket.txt'
        '''
        fp = open('Basket.txt', "a", encoding="utf-8")  # открыть файл для записи с сохранением существующих записей (а- добавление записи в конец списка)
        fp.write(str(basket1.productName) + '\n')
        fp.close()
    #print('Товар добавлен в корзину')

    ch = input('Продолжить покупки (y/n)? ')

    '''
    Вывод итоговых данных о количестве товара и сумме покупки
    '''
    if ch == 'n':
        Basket.basketSum()
