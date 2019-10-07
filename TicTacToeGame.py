import random

def Draw_Board_(_Board_):
       # This will be the function that creates the board

       print('   |   |')
       print(' ' + _Board_[7] + ' | ' + _Board_[8] + ' | ' + _Board_[9])
       print('   |   |')
       print('***********')
       print('   |   |')
       print(' ' + _Board_[4] + ' | ' + _Board_[5] + ' | ' + _Board_[6])
       print('   |   |')
       print('***********')
       print('   |   |')
       print(' ' + _Board_[1] + ' | ' + _Board_[2] + ' | ' + _Board_[3])
       print('   |   |')

def inputPlayerLetter_():
         #Player's choice of Letter_
         Letter_ = ''
         while not (Letter_ == 'X' or Letter_ == 'O'):
             print('Do you want to be X or O on this game?')
             Letter_ = input().upper()

         # Player has first choice, the Computer will follow
         if Letter_ == 'X':
             return ['X', 'O']
         else:
             return ['O', 'X']

def whoGoesFirst():
         # randomization of who goes first
         if random.randint(0, 1) == 0:
             return 'Computer'
         else:
             return 'Player'

def playAgain():
         # This will return true if the player wants to play again
         print('Do you want to play again? (yes or no)')
         return input().lower().startswith('y')

def makeMove(_Board_, Letter_, Move):
         _Board_[Move] = Letter_

def isWinner(b, l):
         #b=Board and l = Letter
         return ((b[7] == l and b[8] == l and b[9] == l) or
         (b[4] == l and b[5] == l and b[6] == l) or
         (b[1] == l and b[2] == l and b[3] == l) or
         (b[7] == l and b[4] == l and b[1] == l) or
         (b[8] == l and b[5] == l and b[2] == l) or
         (b[9] == l and b[6] == l and b[3] == l) or
         (b[7] == l and b[5] == l and b[3] == l) or
         (b[9] == l and b[5] == l and b[1] == l))

def get_Board_Copy(_Board_):
         # Copy of the board
         Duplicate_Board_ = []

         for i in _Board_:
             Duplicate_Board_.append(i)

         return Duplicate_Board_

def isSpaceFree(_Board_, Move):
        #free to move on board
         return _Board_[Move] == ' '

def getPlayerMove(_Board_):
         #Player choice of placing
         Move = ' '
         while Move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(_Board_, int(Move)):
             print('What would be your next move? (1-9)')
             Move = input()
         return int(Move)

def chooseRandomMoveFromList(_Board_, MovesList):
         #validation check
         possibleMoves = []
         for i in MovesList:
             if isSpaceFree(_Board_, i):
                 possibleMoves.append(i)

         if len(possibleMoves) != 0:
             return random.choice(possibleMoves)
         else:
             return None

def getComputerMove(_Board_, ComputerLetter_):
         #Computer's letter
         if ComputerLetter_ == 'X':
             PlayerLetter_ = 'O'
         else:
             PlayerLetter_ = 'X'

         # algorithm used
         for i in range(1, 10):
             Copy = get_Board_Copy(_Board_)
             if isSpaceFree(Copy, i):
                 makeMove(Copy, ComputerLetter_, i)
                 if isWinner(Copy, ComputerLetter_):
                     return i

         # Computer sees what is Player's next possible move to win
         for i in range(1, 10):
             Copy = get_Board_Copy(_Board_)
             if isSpaceFree(Copy, i):
                 makeMove(Copy, PlayerLetter_, i)
                 if isWinner(Copy, PlayerLetter_):
                     return i


         Move = chooseRandomMoveFromList(_Board_, [1, 3, 7, 9])
         if Move != None:
             return Move


         if isSpaceFree(_Board_, 5):
             return 5


         return chooseRandomMoveFromList(_Board_, [2, 4, 6, 8])

def is_Board_Full(_Board_):
         # Return False if space taken
         for i in range(1, 10):
             if isSpaceFree(_Board_, i):
                 return False
         return True


print('Welcome to The Tic Tac Toe Game !')
print("Good Luck!")

while True:

         the_Board_ = [' '] * 10
         PlayerLetter_, ComputerLetter_ = inputPlayerLetter_()
         Turn = whoGoesFirst()
         print('The ' + Turn + ' will have the first move.')
         gameIsPlaying = True

         while gameIsPlaying:
             if Turn == 'Player':
                 # Player will have the turn
                 Draw_Board_(the_Board_)
                 Move = getPlayerMove(the_Board_)
                 makeMove(the_Board_, PlayerLetter_, Move)

                 if isWinner(the_Board_, PlayerLetter_):
                     Draw_Board_(the_Board_)
                     print('Congratulations! You have won the game of Tic Tac Toe!')
                     gameIsPlaying = False
                 else:
                     if is_Board_Full(the_Board_):
                         Draw_Board_(the_Board_)
                         print('This game has been deemed a tie!')
                         break
                     else:
                         Turn = 'Computer'

             else:

                 Move = getComputerMove(the_Board_, ComputerLetter_)
                 makeMove(the_Board_, ComputerLetter_, Move)

                 if isWinner(the_Board_, ComputerLetter_):
                     Draw_Board_(the_Board_)
                     print('The Computer is the Winner! You lose.')
                     gameIsPlaying = False
                 else:
                     if is_Board_Full(the_Board_):
                         Draw_Board_(the_Board_)
                         print('The game has been deemed a tie!')
                         break
                     else:
                         Turn = 'Player'

         if not playAgain():
             break
