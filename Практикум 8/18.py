text = input()
width = int(input())

words = text.split()
currentLine = []
lettersCount = 0

for word in words:
    if lettersCount + len(word) + len(currentLine) <= width:
        currentLine.append(word)
        lettersCount += len(word)
    else:
        spacesCount = width - lettersCount
        gapsCount = len(currentLine) - 1

        if gapsCount > 0:
            spacesPerGap = spacesCount // gapsCount
            extraSpaces = spacesCount % gapsCount

            for i in range(gapsCount):
                print(currentLine[i], end="")
                if i < extraSpaces:
                    print(" " * (spacesPerGap + 1), end="")
                else:
                    print(" " * spacesPerGap, end="")
            print(currentLine[-1])
        else:
            print(currentLine[0])

        currentLine = [word]
        lettersCount = len(word)

print(" ".join(currentLine))
