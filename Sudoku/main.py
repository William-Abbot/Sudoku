import re, functions.printSudokuBoard as printsb, functions.updateBoard as upsb

list1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

printsb.printBoard(list1)
print("\nHello!! Type \'help\' for a list of commands, otherwise, enjoy the game!\n")


next_move = ''
help_commands = {'<move>': '<new value> <letter><number>', 'quit': 'quits game'}


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
    if next_move == 'quit' or next_move == 'exit':
        break
    
    command_list = re.split(r'\s',next_move)
    
    printsb.printBoard(upsb.UpdateBoard(list1, command_list[1], command_list[0]))
    
print("Thanks for playing!\n")
