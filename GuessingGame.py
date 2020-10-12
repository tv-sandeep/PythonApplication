import random

highest = 10
answer = random.randint(1,highest)
print(answer)   #TODO: to remove after tesing
print("Please Guess number between 1 and {}: ".format(highest))
guess = int(input())

if guess == answer:
    print("you got it first time")

else:
    if guess < answer:
        print("please guess higher")
    else:
        print("please guess lower")
    guess = int(input())
    if guess == answer:
        print("well done")
    else:
        print("sorry you are wrong")


#if guess < answer:
#	print("Please guess higher")
#	guess=int(input())
#	if guess==answer:
#		print("welldone you have guessed correctly")
#	else:
#		print("sorry, you are wrong")
#elif guess > answer:
#	print("Please guess lower")
#	guess=int(input())
#	if guess==answer:
#		print("welldone you have guessed correctly")
#	else:
#		print("sorry, you are wrong")
#else:
#	print("Guessed correctly")
