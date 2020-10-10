shopping_list = ["milk" , "bread" , "spam" , "rice" , "dal ", "eggs"]

item_to_find = "spam"
found_at = None

for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_at = index
        break
print("item to be searched is at position {}".format(found_at))
