#ipAddress = input("please enter an ip address")
#print(ipAddress.count("."))

Family_list = ["grandfather" , "grandmother" , "father" , "mother" , "brother" , "sister" , "baby"]
Family_list.append("great grand parents")
for relation in Family_list:
    print("The family consists of " + relation)

even = [2,4,6,8]
odd = [1, 3, 5 , 7]

numbers = even + odd
#numbers.sort()
numbers_in_order = sorted(numbers)
print(numbers_in_order)
if numbers == numbers_in_order:
    print("the lists ar equal")
else:
    print("the lists are not equal")