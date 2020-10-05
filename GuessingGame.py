answer = 5
#print("Please Guess number between 1 and 10: ")
guess = int(input("Please Guess number between 1 and 10: "))

if guess < answer:
	print("Please guess higher")
elif guess > answer:
	print("Please guess lower")
else:
	print("Guessed correctly")
