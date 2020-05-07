# OSS and Git tutorial 
import numpy as np
from time import sleep


# Perform simple arithmetic encoded in an input string:
# '1 + 2' -> 3, or '1 - 2' -> -1.
def compute(expression):
    num0, operator, num1 = expression.split(' ')
    num0, num1 = int(num0), int(num1)
    if operator == '+':
        return num0 + num1
    elif operator == '-':
        return num0 - num1
    else:
        print('unknown operator!')
        return None


# why not?
def inc(x):
	return x + 1

# evil f-ing function
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
            if second_limiter:
                stop = True
            sleep(5)
            if second_limiter:
                stop = True
