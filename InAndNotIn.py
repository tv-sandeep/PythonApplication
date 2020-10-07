parrot = "norwegian Blue"

letter = ""# input("please enter a character: ")

if letter in parrot:
    print("{} is in {}".format(letter,parrot))
else:
    print("i dont need that character")


activity = input("what to do in today: ")

if "cinema" not in activity.casefold():
    print("i want to go cinema")