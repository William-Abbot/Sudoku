#python3!
#solve.py
#William Abbot

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
#Python, please allow implicit references again!!

from solving import solve_depthFirstSearch as dfs, solve_backtracking as backtrack


def solve():
    return None