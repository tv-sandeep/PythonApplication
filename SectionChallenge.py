#print("please select your option")
#print("1: learn python")
#print("2: sleeping")
#print("3: eating")
#print("4: playing")
#print("5: swimming")
#print("0: exit")
option = "6"
while True:
    if option == "0":
        print("exit ")
        break
    elif option in "12345":
        print("you choose {}".format(option))
    #elif option == 1:
    #    print("you choose to learn python")
    #elif option == 2:
    #    print("you choose to sleeping")
    #elif option == 3:
    #    print("you choose to eating ")
    #elif option == 4:
    #    print("you choose to playing")
    #elif option == 5:
    #    print("you choose to swimmimg")
    else:
        print("your choosen option is not in the list")
        print("please select your option")
        print("1: learn python")
        print("2: sleeping")
        print("3: eating")
        print("4: playing")
        print("5: swimming")
        print("0: exit")
    option =  input()
      
    
    