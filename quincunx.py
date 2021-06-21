from random import choice
from time import sleep
from os import system
from termcolor import colored, cprint

N = 1500
n = 20
bins = [0]*n*2

# TODO: dynamic color control
move_color = None #'blue'
quincunx_color = 'blue'
output_color = None #'blue'

move_time = 0.0 #0.005
ball_time = 0.02 #0.1

scale = 'hundreds'

right_move_icon = colored('\\', move_color) #\\
left_move_icon = colored('/', move_color) #/

quincunx = [' '*2*n]*(n)
for k in range(0, n):
    d = k+1
    quincunx[k] = quincunx[k][:n-d] + '/\\'*(d) + quincunx[k][n+d:] 
#quincunx = list(map(lambda row : colored(row, quincunx_color), quincunx))
output = [' '*(n*2)]
for ball in range(N):
    to_print = quincunx[:]
    offset = 0
    for k in range(n):
        sleep(move_time)
        if choice((True, False)):
            to_print[k] = colored(to_print[k][:n+offset], quincunx_color) + right_move_icon + colored(to_print[k][n+offset+1:], quincunx_color)
            offset += 1
        else:
            to_print[k] = colored(to_print[k][:n+offset-1], quincunx_color) + left_move_icon + colored(to_print[k][n+offset:], quincunx_color)
            offset -= 1
        if k == n-1 or move_time > 0:
            system('clear')
            to_print.insert(0, f'Move time: {move_time}. Rest time: {ball_time}. Ball {ball} of {N}.')
            to_print.append(' '*(n+offset)+colored('X', output_color))
            to_print.append(colored('\n'.join(output), output_color))
            print('\n'.join(to_print))
    sleep(ball_time)
    bins[n+offset] += 1
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

