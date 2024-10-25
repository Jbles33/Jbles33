import random
import time


# First level is 7 doors with a danger inside randomly selected (listing user choices here in lists).
def towerDoors(doorNumber):
    playerI = ['1. Squirting flower, 2. Fork, 3. Spoon']
    playerO = ['1. Sword, 2. Try to run, 3. Play dead']
    playerJ = ['1. Holy water, 2. Priest exorcism, 3. Scream']
    playerK = ['1. Search for rope, 2. Try to Climb, 3. Pickup flashlight']
    playerL = ['1. Play dead, 2. Punch bear, 3. Run']
    playerM = ['1. Look for water, 2. Stop. Drop. Roll, 3. Grab fire extinguisher']
    playerN = ['1. Hooray']

    # 7 while loops for each door.
    while doorNumber == 1:
        print('Behind this door is a Dragon, now choose your weapon by the number 1, 2, or 3 \n' + str(playerO))
        playerRes = input()
        # try and except blocks for player response and to loop back if the user has an invalid input
        try:
            playerRes = int(playerRes)
            if playerRes == 1:
                print('\nYou have defeated the dragon')
                return 'Win'
            else:
                print('\nYou were defeated by the dragon')
                return 'Lose'
        except ValueError:
            print('\nThat is an invalid input')

    while doorNumber == 2:
        print('Behind this door is a ghost, now choose your weapon by the number 1, 2, or 3 \n' + str(playerJ))
        playerRes = input()
        try:
            playerRes = int(playerRes)
            if playerRes == 2:
                print('\nYou have defeated the ghost')
                return 'Win'
            else:
                print('\nYou were defeated by the ghost')
                return 'Lose'
        except ValueError:
            print('\nThat is an invalid input')

    while doorNumber == 3:
        print('Behind this door you fall in a dark hole, now choose your weapon by the number 1, 2, or 3 \n'
              + str(playerK))
        playerRes = input()
        try:
            playerRes = int(playerRes)
            if playerRes == 3:
                print('\nYou have escaped the dark hole')
                return 'Win'
            else:
                print('\nYou are stuck in the dark hole')
                return 'Lose'
        except ValueError:
            print('\nThat is an invalid input')

    while doorNumber == 4:
        print('Behind this door is a clown, What weapon would you like? 1, 2, or 3? \n' + str(playerI))
        playerRes = input()
        try:
            playerRes = int(playerRes)
            if playerRes == 1:
                print('\nYou have defeated the clown')
                return 'Win'
            else:
                print('\nYou have been defeated by the clown!')
                return 'Lose'
        except ValueError:
            print('\nThat is an invalid input')

    while doorNumber == 5:
        print('Behind this door is a bear, now choose your weapon by the number 1, 2, or 3 \n' + str(playerL))
        playerRes = input()
        try:
            playerRes = int(playerRes)
            if playerRes == 1:
                print('\nYou survived the bear')
                return 'Win'
            else:
                print('\nYou were eaten by the bear')
                return 'Lose'
        except ValueError:
            print('\nThat is an invalid input')

    while doorNumber == 6:
        print('Behind this door is a pit of fire, now choose your weapon by the number 1, 2, or 3 \n' + str(playerM))
        playerRes = input()
        try:
            playerRes = int(playerRes)
            if playerRes == 3:
                print('\nYou have survived the fire')
                return 'Win'
            else:
                print('\nYou were killed in the fire')
                return 'Lose'
        except ValueError:
            print('\nThat is an invalid input')

    while doorNumber == 7:
        print('Behind this door is another door to escape, type Hooray \n' + str(playerN))
        playerRes = input()
        if playerRes == 'Hooray':
            print(' \nYou are free to move on')
            return 'Win'
        else:
            print(' \n You even failed at that..... ( ._.)')
            return 'Lose'


# maze function
def maze():
    print('\nWelcome to the Scary Maze!')

    # creating the maze with a dictionary
    theMaze = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' ', 10: ' ', 11: ' ', 12: ' ',
               13: ' ', 14: ' ', 15: ' ', 16: ' ', 17: ' ', 18: ' ', 19: ' ', 20: ' ', 21: ' ', 22: ' ', 23: ' ',
               24: ' ', 25: ' '}

    # maze print function
    def printMaze(maze1):
        print('___________')
        print('|' + maze1[1] + '|' + maze1[2] + '|' + maze1[3] + '|' + maze1[4] + '|' + maze1[5] + '|')
        print('|-+-+-+-+-|')
        print('|' + maze1[6] + '|' + maze1[7] + '|' + maze1[8] + '|' + maze1[9] + '|' + maze1[10] + '|')
        print('|-+-+-+-+-|')
        print('|' + maze1[11] + '|' + maze1[12] + '|' + maze1[13] + '|' + maze1[14] + '|' + maze1[15] + '|')
        print('--------   ')

    # while loop for the user playing the maze
    while True:
        countdown(5)
        theMaze[1] = 'o'
        printMaze(theMaze)
        x = 1
        while 0 < x < 16:
            print('Chose a direction to move. [up, down, left, or right]')
            y = input()
            if y == 'up':
                theMaze[x] = ' '
                x -= 5
                theMaze[x] = 'o'
            if y == 'down':
                theMaze[x] = ' '
                x += 5
                theMaze[x] = 'o'
            if y == 'left':
                theMaze[x] = ' '
                x -= 1
                theMaze[x] = 'o'
            if y == 'right':
                theMaze[x] = ' '
                x += 1
                theMaze[x] = 'o'

            printMaze(theMaze)
            if x == 15:
                break

        else:
            print('That is an invalid move. Please try again')

        if x == 15:
            break


# countdown function
def countdown(n):
    while n > 0:
        print(n)
        time.sleep(1)
        n = n - 1
        if n == 0:
            print('Start!')


# Start of game
print('Welcome to Haunted Tower, Would you like to play? Type "y" for yes and "n" for no')
userChoice = input()

name = "default"

# if users inputs y for yes to play game
if userChoice == 'y':
    print('What is your name')
    name = input()

# while loop to see if the user wants to continue playing the game
while userChoice == 'y':
    print(' Welcome ' + name)

    # while loop for the level 1 (Doors) just in case the user has an invalid input
    while True:
        # random number generated for random door for first level
        r = random.randint(1, 7)
        result1 = towerDoors(r)

        # if the user wins the first level he/she will move onto the second (Maze)
        if result1 == 'Win':
            maze()
            print('The maze is finished, You win!')

        # Asking the user if he/she wants to play again, N for "no" and A for "again"
        print('\npress N to quit or press A to play again')
        userInput = input()
        if userInput == 'N' or userInput == 'n':
            print(' See ya next time!')
            userChoice = userInput
            break
        if userInput == "A" or userInput == "a":
            userChoice = "y"
            break


# Saying goodbye to the user if they choose to no longer play
if userChoice == 'n' or 'no':
    print('Alright, Good bye')
else:
    print('Do nothing')