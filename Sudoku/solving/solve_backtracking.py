#python3!
#solve_backtracking.py
#William Abbot

import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
#Python, please allow implicit references again!!

from functions.isValid import isValid
from functions import printSudokuBoard as psb




#list1 = [5,7,1,0,0,0,0,9,6,0,0,0,0,9,0,0,5,0,0,0,0,0,0,5,2,0,7,4,9,0,1,0,0,0,7,0,0,0,0,0,0,7,0,0,0,1,3,0,0,0,0,0,2,0,3,0,4,0,5,9,0,0,0,0,2,8,0,7,1,0,4,0,7,6,5,8,2,0,0,0,0]

def staticCells(grid):
    lst = []
    for i in range(len(grid)):
        if grid[i] != 0:
            lst.append(i)
    return lst

def solve(grid, print):
    static_cells = staticCells(grid)
    num = 1
    letter = 0
    add = False
    c = 0
    test_val = 1
    while c < 81:
        if (grid[c] == 0 or add) and c not in static_cells:
            if not isValid(grid,(chr(letter+65)+str(num)),test_val):
                add = True
                if test_val== 9:
                    add = True
                    grid[c] = 0
                    c -= 1
                    num -= 1
                    if (c + 1) % 9 == 0:
                        num = 9
                    if num % 9 == 0:
                        letter -= 1
                    test_val = grid[c]
                    while c in static_cells:
                        c -= 1
                        num -= 1
                        if (c + 1) % 9 == 0:
                            num = 9
                        if num % 9 == 0:
                            letter -= 1
                        test_val = grid[c]
                else:
                    test_val += 1
            else:
                grid[c] = test_val
                c += 1
                num += 1
                if c % 9 == 0:
                    num = 1
                    letter += 1
                test_val = 0
        else:
            c += 1
            num += 1
            if c % 9 == 0:
                num = 1
                letter += 1
            test_val = 0

        if print:
            psb.printBoard(grid)
            #print(c, num, letter, test_val)
            sys.stdout.write('\r')
            os.system('cls')
            sys.stdout.flush()
    
    psb.printBoard(grid)