#magic8ball

import random

def ball(randNum):
	if randNum == 1:
		return 'Yes'
	elif randNum == 2:
		return 'No'
	elif randNum == 3:
		return 'Ask again later'


messages = ['It is certain',
		'It is decidedly so',
		'Yes definitely',
		'Reply hazy try again',
		'Ask again later',
		'Concentrate and ask again',
		'My reply is no',
		'Outlook no so good',
		'Very doubtful']

# find and index from 0 to the number of messages and print that message
print(messages[random.randint(0, len(messages) - 1)])

