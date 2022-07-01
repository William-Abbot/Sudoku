import re, functions.printSudokuBoard as printsb, functions.updateBoard as upsb
import functions.isValid as valid, functions.solve as solve
import functions.generate as gen

#board = [5,0,1,0,0,0,0,9,6,0,0,0,0,9,0,0,5,0,0,0,0,0,0,5,2,0,7,4,9,0,1,0,0,0,7,0,0,0,0,0,0,7,0,0,0,1,3,0,0,0,0,0,2,0,3,0,4,0,5,9,0,0,0,0,2,8,0,7,1,0,4,0,7,6,5,8,2,0,0,0,0]
board = [0]*81

printsb.printBoard(board)
print("\nHello!! Type \'help\' for a list of commands, otherwise, enjoy the game!\n")


next_move = ''
help_commands = "\"<new value> <letter><number>\": puts <new value> into specified cell\n\"solve\": solves current grid\n\"quit\": quits game\n\"generate\": generates a random sudoku board for you\n"


def delimenate(string):
	templist = []
	for i in string:
		templist.append(int(i))
	return templist


while(True):

    next_move = input("\n>>> ")
    print(" ")#print function prints the input to a NEW LINE, no need to has a \n here
    
    if next_move == 'help':
        print(help_commands)
        continue
    
    if next_move == 'solve':
        if all(x == 0 for x in board):
            print("\nThis Board is empty, try to insert some values\n")
        else:
            solve.solve(board, True)
            printsb.printBoard(board)
        continue

    if next_move == 'generate':
        board = gen.generateBoard(50)
        printsb.printBoard(board)
        continue
        
    if next_move == 'quit' or next_move == 'exit':
        break
    
    command_list = re.split(r'\s',next_move)
    
    try:
        result = valid.isValid(board, command_list[1], command_list[0])
    except IndexError:
        print("invalid command\n")
        continue
    
    if result:
        printsb.printBoard(upsb.UpdateBoard(board, command_list[1], command_list[0]))
    else:
        print("not a valid move\n")   


print("Thanks for playing!\n")