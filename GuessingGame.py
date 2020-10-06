answer = 5
#print("Please Guess number between 1 and 10: ")
guess = int(input("Please Guess number between 1 and 10: "))

if guess < answer:
	print("Please guess higher")
	guess=int(input())
	if guess==answer:
		print("welldone you have guessed correctly")
	else:
		print("sorry, you are wrong")
elif guess > answer:
	print("Please guess lower")
	guess=int(input())
	if guess==answer:
		print("welldone you have guessed correctly")
	else:
		print("sorry, you are wrong")
else:
	print("Guessed correctly")
