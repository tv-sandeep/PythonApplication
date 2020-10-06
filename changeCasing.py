InputStr = input("Enter input string: ")

if InputStr.islower():
    print("Input string is lower case")
elif InputStr.isupper():
    print("Input string is upper case")
else:
    print("Input string is neither lower case nor upper case")

changeCasingTo = int(input("Enter value to convert to upper 1, to lower 2: "))

if changeCasingTo == 1:
    print(InputStr.upper())
elif changeCasingTo == 2:
    print(InputStr.lower())
else:
    print("Enter either 1 or 2")

