string = input()

words = string.split()
firstword = words[0]

for word in words[1:]:                 
    if word != firstword and len(set(word)) == len(word):
        print(word)
