# OSS and Git tutorial 
import numpy as np
from time import sleep

def compute(expression):
    num0, operator, num1 = expression.split(' ')
    if operator == '+':
        return num0 + num1
    elif operator == '-':
        return num0 - num1
    else:
        print('unknown operator!')
        return None

def until_the_cows_come_home():
    the_cows_are_home = False
    while not the_cows_are_home:
        print('Waiting until the cows come home...')
        sleep(5)
        number = np.random.normal(0, 1)
        number_0 = np.random.normal(0, 1)
        if number_0 > 0:
            second_limiter = True
        stop = False
        if number >= 2 and not stop:
            print('Was that a moo?')
            sleep(5)
            if second_limiter:
                stop = True
        if number <= -2 and not stop:
            print('The cows do not want any piece of this.')
            sleep(5)
            if second_limiter:
                stop = True
        if number <2 and number>1.5 and not stop:
            print('Who want\'s them anyway, way too big a carbon footprint!')
            sleep(5)
            if second_limiter:
                stop = True
        if number >-2 and number<-1.8 and not stop:
            print('Seriously, you should kill your kernel. This is just silly...')
            sleep(5)
            if second_limiter:
                stop = True