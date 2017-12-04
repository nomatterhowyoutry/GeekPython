# Створити клас Calc, який буде мати атребут last_result та 4 методи.
# Методи повинні виконувати математичні операції з 2-ма числами, 
# а саме додавання, віднімання, множення, ділення.
# Якщо під час створення екземпляру класу звернутися до атребута 
# last_result він повинен повернути пусте значення
# Якщо використати один з методів - last_result 
# повенен повернути результат виконання попереднього методу.
# Додати документування в клас

class Calc(object):
    ''' Simplest calc class '''
    last_result = 0 # returns last operation result

    def add(self, x ,y):
        ''' addition '''
        self.last_result = x + y

    def sub(self, x ,y):
        ''' substraction '''
        self.last_result = x - y

    def mult(self, x ,y):
        ''' multiplication '''
        self.last_result = x * y

    def div(self, x ,y):
        ''' division '''
        self.last_result = x / y

# t1 = Calc()
# t1.add(2, 5)
# t1.sub(5, 2)
# t1.mult(2, 5)
# t1.div(10, 2)
# print(t1.last_result)

# Створити клас Person, в якому буде присутнім метод __init__ 
# який буде приймати * аргументів, які зберігатиме в відповідні змінні. 
# Методи, які повинні бути в класі Person - show_age, print_name, show_all_information.
# Створіть 2 екземпляри класу Person та в кожному з екземплярів створіть атребут profession.

class Person(object):

    def __init__(self, *args):
        self.args = args

    def show_age(self, age):
        print(age)

    def print_name(self, name):
        print(name)

    def show_all_information(self):
        # print(self.name, self.age)
        print(self.args)

# p1 = Person('Name', 43)
# p2 = Person('Name', 22)
# p1.profession = 'Farmer'
# p2.profession = 'Developer'
# print(p1.show_all_information())
# print(p2.show_all_information())

# Напишіть програму, де клас «геометричні фігури» (figure)
# містить властивість color з початковим значенням white 
# і метод для зміни кольору фігури, а його підкласи «овал» (oval) 
# і «квадрат» (square) містять методи __init__ для завдання 
# початкових розмірів об'єктів при їх створенні.
# Видозмініть програму так, щоб метод __init__ мався 
# в класі «геометричні фігури» та приймав кольор фігури при створенні екземпляру, 
# а методи __init__ підкласів доповнювали його та додавали початкові розміри.


class Figure(object):

    def __init__(self, color):
        self.color = color

    def change_color(self, color):
        self.color = color

class Oval(Figure):

    def __init__(self, r, color):
        Figure.__init__(self, color)
        self.r = r

class Square(Figure):

    def __init__(self, width, height, color):
        Figure.__init__(self, color)
        self.width = width
        self.height = height

# sq = Square(10, 5, 'red')
# print(sq.color)