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

import random

def tell_joke():
    Jokes = [
    '''Doctor: "I'm sorry but you suffer from a terminal illness and have only 10 to live."

Patient: "What do you mean, 10? 10 what? Months? Weeks?!"

Doctor: "Nine."
    ''',
    '''A man asks a farmer near a field,
“Sorry sir, would you mind if I crossed your field instead of going around it? You see, I have to catch the 4:23 train.”

The farmer says, “Sure, go right ahead. And if my bull sees you, you’ll even catch the 4:11 one.”
    ''',
    '''Anton, do you think I’m a bad mother?

My name is Paul.
    ''',
    '''My dog used to chase people on a bike a lot. It got so bad, finally I had to take his bike away.
    ''',
    '''What is the difference between a snowman and a snowwoman?
-
Snowballs.
    ''',
    '''"Mom, where do tampons go?"

"Where the babies come from, darling."

"In the stork?"
    ''']

    print(Jokes[random.randint(0,len(Jokes) - 1)])

from datetime import datetime

def countdown_to_course():
    print(datetime(2017, 11, 1) - datetime.now())

fib = lambda x : 1 if x <= 2 else fib(x - 1) + fib(x - 2)

#-------------------------------------#