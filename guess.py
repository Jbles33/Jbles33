#! python
#John Best
#guess

import random

secretNumber = random.randint(1, 20)

print("I'm thinking of a number between 1 and 20")

for guessesTaken in range(1, 7):
	print("Take a guess")

	try:
		guess = int(input())
		if guess < secretNumber:
			print("\nToo Low")
		elif guess > secretNumber:
			print("\nToo High")
		else:
			print("\nGood job!")
			break

	except ValueError:
		print("\nTHAT IS NOT A NUMBER!")

print("\nGame over!")
