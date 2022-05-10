class Category:
    def __init__(self, categoryNum=int, categoryName=None):
        self.categoryNum = categoryNum    #Номер категории
        self.categoryName = categoryName  #Название категории товара

def choiceCategory():
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