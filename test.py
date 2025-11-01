phrase = str(input("enter your phrase: "))

s = phrase.split()[::-1]
space = " "
print(space.join(s))
