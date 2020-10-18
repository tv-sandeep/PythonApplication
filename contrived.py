numbers = [1, 45, 32, 12 , 60]

for number in numbers:
    if number % 8 == 0:
       print("the numbers are unaccetable")
       break
else:
    print("the numbers are fine")