string = input()

words = string.split()
minlen = len(words[0])

for word in words:
    if len(word) < minlen:
        minlen = len(word)

print(minlen)
