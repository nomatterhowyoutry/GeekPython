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

