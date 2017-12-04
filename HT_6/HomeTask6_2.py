# Напишіть програму в стилі ООП, що задовольняє наступним умовам: 
# у програмі повинні бути два класи та два об'єкта, що належать різним класам; 
# один об'єкт за допомогою методу свого класу повинен так чи інакше змінювати дані іншого об'єкта

class Class1(object):
    """docstring for Class1"""

    def __init__(self, arg):
        super(Class1, self).__init__()
        self.arg = arg

    def shout(self):
        print('{}!'.format(self.arg))

class Class2(Class1):
    """docstring for Class2"""

    def change(self, arg):
        c1.arg = arg

c1 = Class1('This is me')
c2 = Class2('argument')
c1.shout()
c2.change("This isn't me")
c1.shout()

count = 0

# Створіть клас в якому буде атребут який буде рахувати кількість створених екземплярів класів.

class Counter(object):

    def __init__(self):
        global count
        count += 1

    def count(self):
        print(count)

a1 = Counter()
a2 = Counter()
a3 = Counter()
a1.count()

# Створити пустий клас, який називається Thing. 
# Потім створіть об'єкт example цього класу. Виведіть типи зазначених об'єктів.
# Створіть новий клас Thing2 і призначте йому атрибут 
# letters зі значенням 'abc' . Виведіть на екран значення атрибута letters.
# Створіть ще один клас Thing3 . Присвойте значення 'xyz' 
# атрибуту об'єкта, який називається letters. Виведіть на екран значення атрибута letters . 

class Thing(object):
    """docstring for Thing"""

example = Thing()
print(type(example))
print(type(Thing))

class Thing2(object):
    """docstring for Thing2"""
    
    letters = 'abc'

example2 = Thing2()
print(example2.letters)

class Thing3(object):

    letters = 'xyz'

example3 = Thing3()
print(example3.letters)
