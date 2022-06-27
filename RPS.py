from random import choice
player = ''
while player != 'q':
    outcomes = ['It\'s a Tie!', 'You Lose', 'You Win']
    player=input("Throw [R]ock, [P]aper, or [S]cissors (Q to quit.) ").lower()
    if player != 'q':
        computer=choice('rps')
        print('CPU throws a {}'.format(computer))
        print(outcomes[(player!=computer)+(computer+player in 'rpsr')])