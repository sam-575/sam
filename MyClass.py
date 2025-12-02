# -*- coding: utf-8 -*-

class MyClass:
    def __init__(self, color, brend, year):
        self.color = color
        self.brend = brend
        self.year = year
        
myCar = MyClass(input('Цвет: '), input('Модель: '), \
                input('Год: '))


print('Ваш выбор -', myCar.color, myCar.brend, myCar.year)
#print(myCar.brend)
#print(myCar.year)
