import math

pi = math.pi

def AreaCircle(r):
    '''принимает r и возвращает квадрат r умноженный на значение хранящиеся в math.pi'''
    return pi * r * r


def PerimeterCircle(r):
    '''принимает r и возвращает r умноженное на значение хранящиеся в math.pi и умноженное на 2'''
    return 2 * r * pi