import random as rd

#### Functions ####
def fillList( numberOfElementes, lista ):
    for i in range( numberOfElementes ):
        lista.append( i )
        
def printResult(gameHistory_, diceHistoryGame_, numberOfRounds_):
    lastFloor = initialFloor
    for i in range(numberOfRounds_):
        print('Initial Floor: ',initialFloor )
        print(">>>Round: ", i + 1)
        for j in range(epoch):
            if diceHistoryGame_[i][j] == 1 or diceHistoryGame[i][j] == 2:
                print( 'Dice face:',diceHistoryGame_[i][j], 'Up 1 floor! Now the floor is:', gameHistory_[i][j] )
                lastFloor = gameHistory_[i][j]
            elif diceHistoryGame_[i][j] == 3 or diceHistoryGame[i][j] == 4 or diceHistoryGame_[i][j] == 5:
                print( 'Dice face:',diceHistoryGame_[i][j], 'down 1 floor! Now the floor is:', gameHistory_[i][j] )
                lastFloor = gameHistory_[i][j]
            elif diceHistoryGame_[i][j] == 6:
                print( 'Dice face:',diceHistoryGame_[i][j], 'Let\'s roll the dice again!!!')
                print( 'Dice face:', gameHistory_[i][j] - lastFloor,'Up', gameHistory_[i][j] - lastFloor, "floor! Now the flor is:", gameHistory_[i][j] )
        print('\n')

#### Variables ####
floorHistory        = []                #Store the floorHistoryList of every game.
gameHistory         = []
diceHistoryPerRound = []
diceHistoryGame     = []
numberOfRounds      = 500
initialFloor        = 10
currentFloor        = initialFloor     #the current floor starts with 10 but it can be changed by another positive number.
epoch               = 100

fillList( epoch, floorHistory )  #preenche a lista floorHistori para que ela tenha o numero de elementos de epoch
fillList( epoch, diceHistoryPerRound )
def rollDice():
	return rd.randint(1,6)

def copyList(listA):
	return listA
#Loop for 500 games
for i in range( numberOfRounds ):

    rd.seed( version = 2 )              #Seed for aleatory numbers
    floor = rd.randint(0,100)           #set up the floor before the game begins
    currentFloor = initialFloor
    #loop for 100 epoch steps
    for j in range( epoch ):
        
        zebraDice = rd.randint(1,1000)          #There is a 0.1% odds of going to Floor 0 

        if zebraDice == 13:                     #13 is the zebra number.
            currentFloor = 0                    #set up the floor to 0
            floorHistory[ j ] = currentFloor    #store the floor position
            diceHistoryPerRound[ j ] = zebraDice
        else:
            dice = rollDice()           #roll the dice

            if dice == 1 or dice == 2:  #updates floor to floor++
                currentFloor += 1
                floorHistory[ j ] = currentFloor        #store the floor position
                diceHistoryPerRound[ j ] = dice         #store the face of the dice
            elif dice == 3 or dice == 4 or dice == 5:   #updates floor to floor--
                currentFloor -= 1
                floorHistory[ j ] = currentFloor        #store the floor position
                diceHistoryPerRound[ j ] = dice         #store the face of the dice
            elif dice == 6:                             #rool the dice and uptades the floor with new result
                diceHistoryPerRound[ j ] = dice         #store the face of the dice
                dice = rd.randint(1,6)                  #rool the dice again
                currentFloor += dice
                floorHistory[ j ] = currentFloor        #store the floor position
                

    gameHistory.append( floorHistory[ : ] )
    diceHistoryGame.append( diceHistoryPerRound[ : ] )
printResult( gameHistory, diceHistoryGame ,numberOfRounds )