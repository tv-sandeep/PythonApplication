menu = ["idly" , "vada" , "poori" , "chapathi" , "dosa" , "upma" , "pongal"]
number_of_items = len(menu)
print("number of items in menu is {}".format(number_of_items))
iterator = iter(menu)
for i in range(0,number_of_items):
    print(next(iterator))
for item in menu:
    print(item)

