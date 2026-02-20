vowels = "аеёиоуыэюя"

def splitword(word, width):
    for i in range(width, 0, -1):
        if word[i-1] in vowels:
            return word[:i] + "-", word[i:]
    return word[:width] + "-", word[width:]

text = input()
width = int(input())
words = text.split()

for word in words:
    while len(word) > width:
        part, word = splitword(word, width)
        print(part)
    print(word)
