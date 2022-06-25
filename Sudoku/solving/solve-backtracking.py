#python3!
#solve-backtracking.py
#William Abbot

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
#Python, please allow implicit references again!!

from functions import isValid as valid, printSudokuBoard as psb
list1 = [5,0,1,0,0,0,0,9,6,0,0,0,0,9,0,0,5,0,0,0,0,0,0,5,2,0,7,4,9,0,1,0,0,0,7,0,0,0,0,0,0,7,0,0,0,1,3,0,0,0,0,0,2,0,3,0,4,0,5,9,0,0,0,0,2,8,0,7,1,0,4,0,7,6,5,8,2,0,0,0,0]

def solve(grid):
    num = 1
    letter = 0
    for c in range(81):
        add = False
        if grid[c] == 0 or add:
            grid[c] = grid[c]+1
            num += 1
            if (c+1) % 9 == 0:
                num = 1
                letter += 1
            add = False
        if not valid.isValid(grid,(chr(letter+65)+str(num)),grid[c]):
            grid[c] = 0
            num -= 1
            if c % 9:
                letter -= 1
            c -= 1
            add = True
    psb.printBoard(grid)
        #sys.stdout.write('\r')
        #sys.stdout.flush()

solve(list1)