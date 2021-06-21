from random import choice
from time import sleep
from os import system
import sys
from termcolor import colored, cprint

N = 15000
n = 40
bins = [0]*n*2

quincunx = [' '*2*n]*(n)
for k in range(0, n):
    d = k+1
    quincunx[k] = quincunx[k][:n-d] + '/\\'*(d) + quincunx[k][n+d:] 

output = [' '*(n*2)]
for ball in range(N):
    to_print = quincunx[:]
    offset = 0
    for k in range(n):
        if choice((True, False)):
            to_print[k] = to_print[k][:n+offset] + colored('\\', 'blue') + to_print[k][n+offset+1:]
            offset += 1
        else:
            to_print[k] = to_print[k][:n+offset-1] + colored('/', 'blue') + to_print[k][n+offset:]
            offset -= 1
        if k == n-1:
            system('clear')
            print('\n'.join(to_print))
            print(' '*(n+offset)+colored('X', 'blue'))
            print(colored('\n'.join(output), 'blue'))
    sleep(0.1)
    bins[n+offset] += 1
    for i, count in enumerate(bins):
        tens = count // 10
        ones = count % 10
        if tens+1 > len(output):
            output.append(' '*(n*2))
        for row in range(tens):
            output[row] =   (output[row][:i] 
                            + 'X'
                            + output[row][i+1:])
        output[tens] =   output[tens][:i] + (str(ones) if ones != 0 else ' ') \
            + output[tens][i+1:]