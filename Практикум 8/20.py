ones = ["", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
onesFemale = ["", "одна", "две", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
teens = ["десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать",
         "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]
tens = ["", "", "двадцать", "тридцать", "сорок", "пятьдесят",
        "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
hundreds = ["", "сто", "двести", "триста", "четыреста", "пятьсот",
            "шестьсот", "семьсот", "восемьсот", "девятьсот"]

def threeDigitsToWords(number, female=False):    #до 999
    word = ""
    h = number // 100
    t = (number % 100) // 10
    o = number % 10

    if h > 0:
        word += hundreds[h] + " "

    if t == 1:
        word += teens[o] + " "
    else:
        if t > 1:
            word += tens[t] + " "
        if female:
            word += onesFemale[o] + " "
        else:
            word += ones[o] + " "
    return word.strip()

def thousandToWords(number):
    if number == 0:
        return ""
    word = threeDigitsToWords(number, female=True)
    o = number % 10
    t = (number % 100) // 10

    if t == 1:
        word += " тысяч"
    else:
        if o == 1:
            word += " тысяча"
        elif o in [2,3,4]:
            word += " тысячи"
        else:
            word += " тысяч"
    return word.strip()

n = int(input( ))

million = n // 1000000
thousand = (n % 1000000) // 1000
rest = n % 1000

words = ""

if million > 0:
    m = threeDigitsToWords(million)
    o = million % 10
    t = (million % 100) // 10
    if t == 1:
        words += m + " миллионов "
    else:
        if o == 1:
            words += m + " миллион "
        elif o in [2,3,4]:
            words += m + " миллиона "
        else:
            words += m + " миллионов "

if thousand > 0:
    words += thousandToWords(thousand) + " "

if rest > 0:
    words += threeDigitsToWords(rest)

print(words.strip())
