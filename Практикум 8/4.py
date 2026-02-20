string = input()
count = 0

for symbol in string:
    if string.count(symbol) == 3:
        print(symbol)
        break
