#!/usr/bin/env python3
import random
import sys
print('===== Welcome to the magic calculator =====')
print('We got some equations here, but the operator is missing.')
print('Can you help us?')
for i in range(1000):
    print('----- wave {}/1000 -----'.format(i+1))
    rand = random.randint(0, 3)
    operator = ''
    if rand == 0:
        operator = '+'
        a = random.randint(1, 1000)
        b = random.randint(1, 1000)
        print('{} ? {} = {}'.format(a, b, a + b))
    elif rand == 1:
        operator = '-'
        a = random.randint(1, 1000)
        b = random.randint(1, 1000)
        print('{} ? {} = {}'.format(a, b, a - b))
    elif rand == 2:
        operator = '*'
        a = random.randint(1, 1000)
        b = random.randint(1, 1000)
        print('{} ? {} = {}'.format(a, b, a * b))
    elif rand == 3:
        operator = '/'
        a = random.randint(1, 1000)
        b = random.randint(1, 1000)
        print('{} ? {} = {}'.format(a, b, a / b))
    ans = input('which operator(+/-/*)?')
    if (ans != operator):
        print('Your math is bad...')
        sys.exit()
print("flag")
sys.exit()