def season1(n):
    #season(1-12)
    a = {'Winter': (1, 2, 12),'Spring': (3, 4, 5),'Summer': (6, 7, 8),'Autumn': (9, 10, 11)}
    for k,v in a.items():
        if n in v:
            return k
    return 'Wrong Number!'

def season2(n):
    #season(1-12)
    if n == 1 or 2 or 12:
        return 'Winter'
    elif n == 3 or 4 or 5:
        return 'Spring'
    elif n == 6 or 7 or 8:
        return 'Summer'
    elif n == 9 or 10 or 11:
        return 'Autumn'
    return 'Wrong Number!'

def season3(n):
    #season(1-12)
    return 'Wrong Number!'

#-------------------------------------#

def task2(x, *args):
    #task2(3, 1)
    if args:
        return x + sum(args)
    else:
        return x**2

#-------------------------------------#

def func1(x):
    if x > 0:
        return x * func1(x - 1)
    else:
        return 1

def func2(x):
    return (x/3.14)*2

def func3(x):
    return 'Hello World!' * int(x)

def func4(x):
    #Do not use big numbers
    print(func3(func2(func1(x))))

#-------------------------------------#

def task4(x, y):
    if x > y:
        print(x, 'greater than', y, 'for', x-y)
    elif y > x:
        print(y, 'greater than',x , 'for', y-x)
    else:
        print(x, 'is equal to', y)

#-------------------------------------#

import re

def task5(s):
    l = len(s)
    if l < 30:
        result = re.sub(r'[0-9]+', '', s)
        numbers = re.findall(r'[0-9]+', s)
        print(sum([int(i) for i in numbers]), result)
    elif l > 50:
        print(len(re.sub(r'[0-9]+', '', s)))
    elif 30 <= l <= 50:
        print(len(re.sub(r'[0-9]+', '', s)), len(re.findall(r'[0-9]+', s)))
    else:
        print(s * 100)

#-------------------------------------#
