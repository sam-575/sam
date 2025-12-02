# -*- coding: utf-8 -*-
# Sum of numbers

print('Enter word "stop" for result')
summ = 0
while True:
    x = input('Enter num: ')
    if x == 'stop':
        break
    x = int(x)
    summ += x
print('Summ number:', summ)
input()

