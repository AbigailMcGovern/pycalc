# OSS and Git tutorial 
import numpy as np
# Perform simple arithmetic encoded in an input string:
# '1 + 2' -> 3, or '1 - 2' -> -1.
def compute(expression):
    values = expression.split(' ')
    num0 = int(values[0])
    operator = values[1]
    num1 = int(values[2])
    if operator == '+':
        return num0 + num1
    elif operator == '-':
        return num0 - num1
    else:
        print('unknown operator!')
        return None

# making another comment


def inc(x):
	return x + 1

# evil f-ing function
def until_the_cows_come_home():
    the_cows_are_home = False
    while not the_cows_are_home:
        print('Waiting until the cows come home...')
        number = np.random.normal(0, 1)
        number_0 = np.random.normal(0, 1)
        if number_0 > 0:
            second_limiter = True
        stop = False
        if number >= 2 and not stop:
            print('Was that a moo?')
            if second_limiter:
                stop = True
        if number <= -2 and not stop:
            print('The cows do not want any piece of this.')
            if second_limiter:
                stop = True
        if number <2 and number>1.5 and not stop:
            print('Who want\'s them anyway, way too big a carbon footprint!')
            if second_limiter:
                stop = True
        if number >-2 and number<-1.8 and not stop:
            print('Seriously, you should kill your kernel. This is just silly...')
            if second_limiter:
                stop = True



