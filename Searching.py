shopping_list = ["milk" , "bread" , "spam" , "rice" , "dal ", "eggs"]

item_to_find = "spam"
found_at = None

#for index in range(len(shopping_list)):
#    if shopping_list[index] == item_to_find:
#        found_at = index
#        break

if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)

if found_at is not None:
    print("item to be searched is at position {}".format(found_at))
else:
    print("{} is not found".format(item_to_find))
