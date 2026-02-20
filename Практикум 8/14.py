podskazka = input()
word = input()

for i in range(25):
    print()

hidden = "*" * len(word)
attempts = 10

while attempts > 0:
    print(podskazka)
    print(hidden)

    choice = input("Буква или слово (0 - буква, 1 - слово)? ")

    if choice == "0":
        letter = input()

        temp = ""
        for i in range(len(word)):
            if word[i] == letter:
                temp += letter
            else:
                temp += hidden[i]

        hidden = temp
        attempts -= 1

        if hidden == word:
            print("Победа!")
            break

    else:
        guess = input()
        if guess == word:
            print("Победа!")
        else:
            print("Проигрыш!")
        break

if attempts == 0 and hidden != word:
    print("Проигрыш!")
