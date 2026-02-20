string = input()
count = 1
maxcount = 1

for symbol in range(1, len(string)):
    if string[symbol] == string[symbol - 1]:
        count += 1
    else:
        if count > maxcount:
            maxcount = count
        count = 1                              #начало новой серии

if count > maxcount:
    maxcount = count

print(maxcount)

