from random import choice
from time import sleep
from os import system
import sys
from termcolor import colored, cprint

N = 1000
n = 15
middle = n
bins = [0]*n*2

quincunx = [' '*2*n]*(n)
for k in range(0, n):
    d = k+1
    quincunx[k] = quincunx[k][:middle-d] + '/\\'*(d) + quincunx[k][middle+d:] 

output = [' '*(n*2)]
for ball in range(N):
    to_print = quincunx[:]
    offset = 0
    for k in range(n):
        #to_print = ' '*2*n
        if choice((True, False)):
            to_print[k] = to_print[k][:middle+offset] + colored('\\', 'blue') + to_print[k][middle+offset+1:]
            offset += 1
        else:
            to_print[k] = to_print[k][:middle+offset-1] + colored('/', 'blue') + to_print[k][middle+offset:]
            offset -= 1
        sleep(0.01)
        system('clear')
        print('\n'.join(to_print))
        if k == n-1:
            print(' '*(middle+offset)+colored('X', 'blue'))
        else:
            print(' ')
        print(colored('\n'.join(output), 'blue'))
    bins[middle+offset] += 1
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
    #sleep(0.05)
    #print(list(enumerate(bins)))