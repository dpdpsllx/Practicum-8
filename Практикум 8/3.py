string = input()

difletters = set()

for symbol in string:
    if symbol.isalpha():
        difletters.add(symbol.lower())

print(len(difletters))
