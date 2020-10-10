parrot = "Norwegian Blue"
word = ""
for character in parrot:
    print(character)
    word = word + character
print(word)

number = input("please enter a series of numbers using seperators: ")
seperators = ""
for char in number:
    if not char.isnumeric():
        print(char)
        seperators = seperators + char

print(seperators)

values = "".join(char if char not in seperators else " " for char in number).split()
print(values)
print(sum([int(val) for val in values]))


word = ""
for char in number:
    if char not in seperators:
        word  = word + char
    #else:
    #    word  = word + " "
print(word)
print(sum([int(val) for val in word]))

res = 0
for val in word:
    res = res + int(val)
print(res)