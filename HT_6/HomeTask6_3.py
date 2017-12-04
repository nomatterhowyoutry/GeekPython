# Створіть клас, який називається DefaultClass що має атрибути об'єкту name, symbol number .
# Виведіть атребути.
# Створіть словник з наступними ключами і значеннями:
# 'name': 'Vasya', 'l_name': 'Pupkin', 'age': 20 . 
# Далі створіть об'єкт з ім'ям user класу DefaultClass1за допомогою цього словника.
# Для класу DefaultClass1 визначте метод з ім'ям print_info() ,
# що виводить на екран значення атрибутів об'єкта (name , l_name та age ).

class DefaultClass(object):
    name = ''
    symbol_number = 0

dictionary = {'name': 'Vasya', 'l_name': 'Pupkin', 'age': 20}

class DefaultClass1(DefaultClass):

    def print_info(self):
        print(self.name)

user = DefaultClass()
user1 = DefaultClass1()
user1.name = dictionary

user1.print_info()
        
        
# Створіть 3 класи, 2 з яких будуть успадковуватись один від одного! 
# В суперкласі мається метод __init__ який приймає 2 атребути.
# Перегрузіть конструктор класу в дочірньому класі так, щоб додався ще один атребут. 

class Class1(object):
    """docstring for Class1"""
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

class Class2(Class1):
    """docstring for Class2"""
    def __init__(self, arg3):
        super(Class1, Class1.__init__(self, 10, 20))
        self.arg3 = arg3

    def test(self):
        print(self.arg1, self.arg2, self.arg3)
        
class Class3(Class2):
    """docstring for Class3"""
    def __init__(self):
        super(Class2, Class2.__init__(self, 30))

    def test(self):
        print(self.arg1, self.arg2, self.arg3)

cl1 = Class1(10, 20)
cl2 = Class2(30)   
cl3 = Class3()
cl2.test()
cl3.test()