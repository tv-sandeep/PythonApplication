low = 0
high = 1000

print("please enter between numbers {} to {}".format(low,high))
input("please enter to start")

guesses = 1
while True:
    print("\t Guessing in the range of {} to {}".format(low,high))
    guess = (low + high) // 2
    high_low = input("my guess is {} , should i guess higher or lower?"
                     "enter h or l ,or c if my guess was correct: "
                     .format(guess)).casefold()
    if high_low == "h":
        # guess higher.The low end of the range becomes 1 greater than the guess.
        low = guess + 1
    elif high_low == "l":
        #guess lower.The high end of the range becomes 1 less than the guess.
        high = guess - 1
    elif high_low =="c":
        print("i got it in {} guesses!".format(guesses))
        break
    else:
        print("please enter h,l or c: ")
    guesses = guesses + 1