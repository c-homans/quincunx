import sys
import argparse
import colorama
from random import choice
from time import sleep
from os import system
from termcolor import colored
colorama.init()  # helps print termcolor on non-unix systems

def get_arguments():
    parser = argparse.ArgumentParser(description='Configuration for the quincunx.')
    parser.add_argument('-n', default=30)
    parser.add_argument('-B', default=500)
    parser.add_argument('-scale', default='tens')
    parser.add_argument('-move', default=0)
    parser.add_argument('-rest', default=0.2)
    parser.add_argument('-move_color', default=None)
    parser.add_argument('-quincunx_color', default=None)
    parser.add_argument('-output_color', default=None)
    parser.add_argument('-lmove', default='#')
    parser.add_argument('-rmove', default='#')
    return parser.parse_args()

clear = '\033c'
def draw_frame():
    to_print = qc[:]
    to_print.insert(
        0, f'Move time: {move_time}. Rest time: {ball_time}. Ball {ball} of {N}.')
    to_print.append(' '*(n+pos)+colored('+', output_color))
    to_print.append(colored('\n'.join(output), output_color))
    to_print.insert(0, clear)
    print('\n'.join(to_print))

def create_raw_quincunx():
    raw_quincunx = [' '*2*n]*(n)
    for k in range(0, n):
        d = k+1
        raw_quincunx[k] = ( raw_quincunx[k][:n-d]
                          + '/\\'*(d)
                          + raw_quincunx[k][n+d:])
    return raw_quincunx

def update_quincunx(k, pos):
    sleep(move_time)
    #print(to_print)
    if choice((True, False)):
        qc[k] = colored(raw_qc[k][:n+pos], quincunx_color) + right_move_icon + colored(raw_qc[k][n+pos+1:], quincunx_color)
        pos += 1
    else:
        qc[k] = colored(raw_qc[k][:n+pos-1], quincunx_color) + left_move_icon + colored(raw_qc[k][n+pos:], quincunx_color)
        pos -= 1
    if k == n-1 or (move_time > 0 and k % 3 == 0):
        draw_frame()
    return pos

def update_output_bin(i, count):
    hunds = count // 100
    tens_mod_100 = (count % 100) // 10
    tens = count // 10
    ones = count % 10
    (big, small) = (hunds, tens_mod_100) if scale == 'hundreds' else (tens, ones)
    if big+1 > len(output):
        output.append(' '*(n*2))
    for row in range(big):
        output[row] = ( output[row][:i]
                      + 'X'
                      + output[row][i+1:])
    output[big] = ( output[big][:i]
                  + (str(small) if count > 0 else ' ')
                  + output[big][i+1:] )

args = get_arguments()
n = args.n
N = args.B
scale = args.scale
move_time = args.move #0.005
ball_time = args.rest #0.1
move_color = args.move_color #'blue'
quincunx_color = args.quincunx_color #None
output_color = args.output_color #'blue'
right_move_icon = colored(args.rmove, move_color)  # \\
left_move_icon = colored(args.lmove, move_color)  # /

raw_qc = create_raw_quincunx()
bins = [0]*(n*2)
output = [' '*(n*2)]

for ball in range(1, N+1):
    pos = 0
    qc = list(map(lambda s : colored(s, quincunx_color), raw_qc))
    for k in range(n):
        sleep(move_time)
        pos = update_quincunx(k, pos) 
    bins[n+pos] += 1    
    for i, count in enumerate(bins):
        update_output_bin(i, count)
    draw_frame()
    sleep(ball_time)
