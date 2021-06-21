from random import choice
from time import sleep
from os import system
#import sys
from termcolor import colored, cprint

N = 15000
n = 20
bins = [0]*n*2

# TODO: dynamic color control
move_color = 'blue'
quincunx_color = None
output_color = 'blue'

right_move_icon = colored('\\', move_color) #\\
left_move_icon = colored('/', move_color) #/

quincunx = [' '*2*n]*(n)
for k in range(0, n):
    d = k+1
    quincunx[k] = quincunx[k][:n-d] + '/\\'*(d) + quincunx[k][n+d:] 
quincunx = list(map(lambda row : colored(row, quincunx_color), quincunx))
output = [' '*(n*2)]
for ball in range(N):
    to_print = quincunx[:]
    offset = 0
    for k in range(n):
        if choice((True, False)):
            to_print[k] = to_print[k][:n+offset] + right_move_icon + to_print[k][n+offset+1:]
            offset += 1
        else:
            to_print[k] = to_print[k][:n+offset-1] + left_move_icon + to_print[k][n+offset:]
            offset -= 1
        if k == n-1:
            system('clear')
            print('\n'.join(to_print))
            print(' '*(n+offset)+colored('X', output_color))
            print(colored('\n'.join(output), output_color))
    #sleep(0.01)
    bins[n+offset] += 1
    for i, count in enumerate(bins):
        hunds = count // 100
        tens = (count % 100)// 10
        ones = count % 10
        scale = 'hundreds'
        if scale =='tens':
            if tens+1 > len(output):
                output.append(' '*(n*2))
            for row in range(tens):
                output[row] =   (output[row][:i] 
                                + 'X'
                                + output[row][i+1:])
            output[tens] = output[tens][:i] + (str(ones) if ones > 0 else ' ') + output[tens][i+1:]
        elif scale == 'hundreds':
            if hunds+1 > len(output):
                output.append(' '*(n*2))
            for row in range(hunds):
                output[row] =   (output[row][:i] 
                                + 'X'
                                + output[row][i+1:])
            output[hunds] = output[hunds][:i] + (str(tens) if tens > 0 else ' ') + output[hunds][i+1:]

