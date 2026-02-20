text = input("Введите текст: ")

count = 0
correct = True

for skobka in text:
    if skobka == "(":
        count += 1
    elif skobka == ")":
        count -= 1

    if count < 0:
        correct = False
        break

if count != 0:
    correct = False

if correct:
    print("Скобки расставлены правильно")
else:
    print("Скобки расставлены неправильно")
