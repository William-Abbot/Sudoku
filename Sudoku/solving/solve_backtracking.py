#python3!
#solve_backtracking.py
#William Abbot

from nntplib import GroupInfo
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
    add = False
    c = 0
    test_val = 0
    while c < 81:
        if grid[c] == 0 or add:
            test_val += 1
            add = False
            if not valid.isValid(grid,(chr(letter+65)+str(num)),test_val) or test_val == 9:
                add = True
                if test_val== 9:
                    grid[c] = 0
                    c -= 1
                    num -= 1
                    if num % 9 == 0:
                        letter -= 1
                    test_val = grid[c]
            else:
                grid[c] = test_val
                c += 1
                num += 1
                if (num-1) % 9 == 0:
                    num = 1
                    letter += 1
                test_val = 0
        else:
            c += 1
            num += 1
            if (num-1) % 9 == 0:
                num = 1
                letter += 1
            test_val = 0

        psb.printBoard(grid)
        #sys.stdout.write('\r')
        sys.stdout.flush()
        os.system('cls')

solve(list1)