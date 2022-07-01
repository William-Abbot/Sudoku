#!pyhton3
#generate.py
#william Abbot

import sys, os

from . import isValid, printSudokuBoard as psb
import random

index_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80]
position_list = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8', 'I9']

def getStaticCells(difficulty):
    return random.sample(index_list, difficulty)

def allValid(grid, static_cells):
    return all([isValid.isValid(grid, position_list[x], grid[x]) for x in static_cells])

def generateBoard(difficulty):
    tempList = [5, 7, 1, 2, 8, 3, 4, 9, 6, 2, 4, 3, 7, 9, 6, 8, 5, 1, 6, 8, 9, 4, 1, 5, 2, 3, 7, 4, 9, 6, 1, 3, 2, 5, 7, 8, 8, 5, 2, 9, 4, 7, 1, 6, 3, 1, 3, 7, 5, 6, 8, 9, 2, 4, 3, 1, 4, 6, 5, 9, 7, 8, 2, 9, 2, 8, 3, 7, 1, 6, 4, 5, 7, 6, 5, 8, 2, 4, 3, 1, 9]
    static_cells = getStaticCells(difficulty)
    for x in static_cells:
        tempList[x] = 0
    return tempList
    '''
    while not allValid(tempList, static_cells):
        tempList = [0]*81
        static_cells = getStaticCells(difficulty)
        for t in range(81):
            if t in static_cells:
                tempList[t] = random.randint(1,9)
        psb.printBoard(tempList)
        sys.stdout.write('\r')
        os.system('cls')
        sys.stdout.flush()
    return tempList
    '''
