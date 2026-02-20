string = input()

words = string.split()
words.sort(key = len, reverse = False)

print(" ".join(words))
