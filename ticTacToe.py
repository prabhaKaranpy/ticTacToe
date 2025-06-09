board = ['-' ,'-' ,'-',
	 '-' ,'-' ,'-',  
	 '-' ,'-' ,'-']
winner = None #winner is none by default
pp = 'X' #present player (X) starts first
game = True #for confirming the game is still going

def boardShow(): #2
	print(board[0] + ' | ' + board[1] + ' | ' + board[2])
	print(board[3] + ' | ' + board[4] + ' | ' + board[5])
	print(board[6] + ' | ' + board[7] + ' | ' + board[8]) 
	
	
	
#main game play starts here
#10 functions were declared here and has been called

def gamePlay(): #1
	boardShow() #to display the board
	while game:
		turnTurn(pp) #for handling the turns
		detectIfGameOver() #results
		flipPlayer() #changes the turn of player
	
	if winner == 'X' or winner == 'O' :
		print()
		print(winner + ' Wins !') #results
		
	elif winner == None:
		print() 
		print('Game Tied !') #results
		
def turnTurn(player): #3
	print(player + '\'s turn : ') #conveys turn
	position = input('\n\nChoose your position from 1 to 9 : ') #user input
	ok = False #for checking the valid info
	while not ok:
		while position not in ['1','2','3','4','5','6','7','8','9']: #if the input is wrong, the loop exists
			position = input(' \n\nYou entered the position was incorrect!!! Please choose your position from 1 to 9 : ')
		position = int(position) - 1
		
		if board[position] == '-':
			ok = True
			board[position] = player
		else:
			print('\n\nThis position has already been filled, Try again : ')
		
		
		 
		#(-) should be replaced by user input which was stored in the variable (position)
		boardShow()
		#displays the updated board
		
def detectIfGameOver(): #4
    #for results either win or tie 
	detectIfWin() #checks win
	detectIfTie() #checks tie
	
def detectIfWin(): #5
	
	global winner 
	#this is global variable accessed by the key word (global)
	'''I written the names of the 
	variables and functions(dhoni, rohit, jadeja - they're crickets) in the function
	detectIfWin is for fun.
	
	Actually dhoni for columns,
	rohit for rows,
	jadeja for diagonals.
	
	(Which means dhoni's straight six,
	rohit's pull shot,
	jadeja's hammering sixes in leg side and 
	over covers.) 
	'''
	
	dhoni = checkDhoni()
	rohit = checkRohit()
	jadeja = checkJadeja()
	
	if dhoni:
		winner = dhoni
	elif rohit:
		winner = rohit
	elif jadeja:
		winner = jadeja
	else:
		winner = None
		
def checkDhoni(): #6
	global game
	
	dhoniBat = board[0] == board[3] == board[6] != '-'
	dhoniCaptain = board[1] == board[4] == board[7] != '-'
	dhoniWk = board[2] == board[5] == board[8] != '-'
	
	
	if dhoniBat or dhoniCaptain or dhoniWk:
		game = False
	if dhoniBat:
		return board[0]
	elif dhoniCaptain:
		return board[1]
	elif dhoniWk:
		return board[2]
	else:
		return None
	
def checkRohit(): #7
	global game
	
	rohitBat = board[0] == board[1] == board[2] != '-'
	rohitCaptain = board[3] == board[4] == board[5] != '-'
	rohitField = board[6] == board[7] == board[8] != '-'
	
	
	if rohitBat or rohitCaptain or rohitField:
		game = False
	if rohitBat:
		return board[0]
	elif rohitCaptain:
		return board[3]
	elif rohitField:
		return board[6]
	else:
		return None
		
def checkJadeja(): #8 cool jadeja's number'
	global game
	
	jadejaBat = board[2] == board[4] == board[6] != '-'
	jadejaBall = board[0] == board[4] == board[8] != '-'
	
	if jadejaBat or jadejaBall:
		game = False
	if jadejaBat:
		return board[2]
	elif jadejaBall:
		return board[0]
	else:
		return None
		
		
def detectIfTie(): #9
	global game
	
	if '-' not in board: #checking for tie
		game = False
		return True
	else:
		return False 
	
	
def flipPlayer(): #10
	global pp
	
	if pp == 'X': 
	#if the player is X then the turn shifts to player O
		pp = 'O'
	elif pp == 'O':
	#if the player is O then the turn shifts to player X
		pp = 'X' 

#finally calling the main game play function
gamePlay()
