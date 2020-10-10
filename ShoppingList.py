
shopping_list = ["milk" , "bread" , "spam" , "rice" , "dal ", "eggs"]

#for item in shopping_list:
#    if item!= "spam":
#        print("buy " +item)


for item in shopping_list:
    if item == "spam":
        break

    print("buy " +item)

print("")
for item in shopping_list:
    if item == "spam":
        continue

    print("buy " +item)
