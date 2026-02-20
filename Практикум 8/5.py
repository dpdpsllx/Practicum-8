string1 = input()
string2 = input()
string3 = input()

allsymbols = string1 + string2 + string3

for symbol in allsymbols:
    count = 0
    if symbol in string1:
        count += 1
    if symbol in string2:
        count += 1
    if symbol in string3:
        count += 1

    if count == 1:
        print(symbol, end = ' ')
