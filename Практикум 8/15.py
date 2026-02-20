secret = input()   

for chislo in range(25):
    print()

attempts = 10

while attempts > 0:
    guess = input()

    bulls = 0
    cows = 0

    for chislo in range(4):
        if guess[chislo] == secret[chislo]:
            bulls += 1
        elif guess[chislo] in secret:
            cows += 1

    print("Быков:", bulls, "Коров:", cows)

    if bulls == 4:
        print("Победа!")
        break

    attempts -= 1

if attempts == 0 and bulls != 4:
    print("Проигрыш!")
