#print(range(100))

#my_list = list(range(10))
#print(my_list)

#even = list(range(0,10,2))
#odd = list(range(1,10,2))

#print(even)
#print(odd)
my_string ="abcdefghijklmnopqrstuvwxyz"

print(my_string.index('e'))
print(my_string[4])

small_decimals = range(0, 10)

print(small_decimals)
print(small_decimals.index(3))

odd = range(1 ,100000,  2)
print(odd)
print(odd[985])

sevens = range(7, 1000000 , 7)
x = int(input("please enter the number less than one millon: "))
if x in sevens:
    print("{} is divisible by 7".format(x))
else:
    print("the number is not divisible by 7")

decimals = range(0,100)
print(decimals)

my_range = decimals[3:40:3]
print(my_range)

for i in my_range:
    print(i)

print("=" *80)

for i in range(3,40,3):
    print(i)

print(my_range == range(3,40,3))
