board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

player1 = ["", "not"]
player2 = ["", "not"]


def displayBoard(board):
  print(board[0] + '|' + board[1] + '|' + board[2]  + '      index values      ' + '1' + '|'+ '2' + '|' + '3')
  print('-' + '-' + '-' + '-' + '-'  +  '                        ' + '-' + '-'+ '-' + '-' + '-')
  print(board[3] + '|' + board[4] + '|' + board[5]  +  '                        ' + '4' + '|'+ '5' + '|' + '6')
  print('-' + '-' + '-' + '-' + '-'  +  '                        ' + '-' + '-'+ '-' + '-' + '-')
  print(board[6] + '|' + board[7] + '|' + board[8]  + '                        ' + '7' + '|'+ '8' + '|' + '9')



def pickPlayer():
  print("Welcome to tic-tac-toe")
  
  value = ""
  ready = ""
  playerW = None
  
  while True:
    value = input("Player 1:  do you want to be X or O:  ").upper()
    print(value)
    if value == 'X':
        break  # Exit loop if input is valid
    elif value == 'O':
      break  # Exit loop if input is valid
    else:
        print("Invalid Pick X or O")
    
  player1[0] = value
  player1[1] = "it"
  
  if value == 'X':
    player2[0] = 'O'
  else:
    player2[0] = 'X'
    
    
  while True:
    ready = input("Are you ready to play: Yes or No  ").lower()
    if ready == 'yes':
        break  # Exit loop if input is valid
    elif ready == 'no':
      break  # Exit loop if input is valid
    else:
        print("Invalid Pick Yes or No")
    
  displayBoard(board)
  
  for num in board:
    playerI = 10
    
    idx = range(1, 10)
    
    while True:
      playerI = int(input("Input your index (1-9): "))  # Get input and convert to integer
      if playerI in idx:
        print("        ")
        print("        ")
        print("        ")
        print("        ")
        break  # Exit loop if input is valid

      else:
          print("Invalid input. Please enter a number between 1 and 9.")
  
    
      
    
    if playerI in idx:
      if player1[1] == "it":
        board[playerI - 1] = player1[0]
        
        player1[1] = "not"
        player2[1] = "it"
        
        displayBoard(board)
        
        playerW = checkWinner(board, "player 1")
      elif player2[1] == "it":
        board[playerI - 1] = player2[0]
        
        player2[1] = "not"
        player1[1] = "it"
        
        displayBoard(board)
        
        playerW = checkWinner(board, "player 2")
      else:
        print("haa")
    
    if playerW != "d" and playerW[0] in ("X", "O"): 
      break
    
  if playerW != "d" and playerW[0] in ("X", "O"):
    displayWinner(playerW)
    
        
        
def checkWinner(board, player):
    # Define winning combinations
    winning_combinations = [
        [0, 1, 2],  # Top row
        [3, 4, 5],  # Middle row
        [6, 7, 8],  # Bottom row
        [0, 3, 6],  # Left column
        [1, 4, 7],  # Middle column
        [2, 5, 8],  # Right column
        [0, 4, 8],  # Diagonal from top-left to bottom-right
        [2, 4, 6]   # Diagonal from top-right to bottom-left
    ]
    
    for combination in winning_combinations:
        a, b, c = combination
        if board[a] == board[b] == board[c] and board[a] != " ":
            return [board[a], player]
    
    return "d"    
          
          
def displayWinner(params):
  print(f"{params[1]} is the winner with the avatar of {params[0]}")   
  
  playAgain = input("Do you want to play again: Yes or No  =>   ").lower()
  if playAgain == 'yes':
    board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    displayBoard(board)  
    pickPlayer()
  elif playAgain == 'no':
    print("Thank you for playing my Tic-Tac-Toe")
  else:
      print("Invalid Pick Yes or No")    
          
          
          
def welcomeAndSelect():
  displayBoard(board)
  pickPlayer()
  
welcomeAndSelect()
  
    
       

