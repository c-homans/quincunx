from random import choice
from time import sleep
from os import system
from termcolor import colored, cprint

N = 300
n = 20
bins = [0]*n*2

# TODO: command-line control
move_color = None #'blue'
quincunx_color = None #None
output_color = None #'blue'

move_time = 0 #0.005
ball_time = 0.05 #0.1

scale = 'hundreds'

right_move_icon = colored('#', move_color) #\\
left_move_icon = colored('#', move_color) #/

def format(string, color):
    if color:
        return colored(string, color)
    else:
        return string

raw_quincunx = [' '*2*n]*(n)
for k in range(0, n):
    d = k+1
    raw_quincunx[k] = raw_quincunx[k][:n-d] + '/\\'*(d) + raw_quincunx[k][n+d:] 
output = [' '*(n*2)]
for ball in range(1, N+1):
    pos = 0
    quincunx = list(map(lambda s : colored(s, quincunx_color), raw_quincunx))
    for k in range(n):
        sleep(move_time)
        #print(to_print)
        if choice((True, False)):
            quincunx[k] = format(raw_quincunx[k][:n+pos], quincunx_color) + right_move_icon + format(raw_quincunx[k][n+pos+1:], quincunx_color)
            pos += 1
        else:
            quincunx[k] = format(raw_quincunx[k][:n+pos-1], quincunx_color) + left_move_icon + format(raw_quincunx[k][n+pos:], quincunx_color)
            pos -= 1
        if k == n-1 or move_time > 0:
            system('clear')
            to_print = quincunx[:]
            to_print.insert(0, f'Move time: {move_time}. Rest time: {ball_time}. Ball {ball} of {N}.')
            to_print.append(' '*(n+pos)+colored('X', output_color))
            to_print.append(colored('\n'.join(output), output_color))
            print('\n'.join(to_print))
    sleep(ball_time)
    bins[n+pos] += 1
    for i, count in enumerate(bins):
        hunds = count // 100
        tens_mod_100 = (count % 100) // 10
        tens = count // 10
        ones = count % 10

        (big, small) = (hunds, tens_mod_100) if scale == 'hundreds' else (tens, ones)

        if big+1 > len(output):
            output.append(' '*(n*2))
        for row in range(big):
            output[row] =   (output[row][:i] 
                            + 'X'
                            + output[row][i+1:])
        output[big] = output[big][:i] + (str(small) if count > 0 else ' ') + output[big][i+1:]

