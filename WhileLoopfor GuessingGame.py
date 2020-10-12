import random

answer = random.randint(1,10)

print("please enter the number between 1 and 10: ")
guess =0
guess = int(input())

while guess!=answer and guess != 0:
    if(guess>answer):
        print("please guess lower")
    else:
        print("please guess higher")
    guess = int(input())

if guess == 0:
    print("you are quit")
else:
    print("you guessed correctly")