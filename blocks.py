for i in range(1,13):
    print("No. {} squared is {} and cubed is {:4}".format(i, i**2, i**3))
    print("*" * 80)

name = input("please enter your name: ")
age = int(input("how old are you, {0} ".format(name)))
print(age)

# if age >= 18:
#     print("you are old enough to vote")
#     print("please put an X in the box")
# else:
#     print("please come back in {0} years".format(18-age))

if age <18:
    print("please come back in {0} years".format(18-age))
elif age==900:
    print("sorry, yoda , you die in return of the jedi")
else:
    print("you are old enough to vote")
    print("please put an X in the box")