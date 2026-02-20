cities = input().split()

players = ["Петя", "Вася"]

for city in range(1, len(cities)):
    if cities[city][0].lower() != cities[city-1][-1].lower():
        print(players[(city + 1) % 2])  
        break
else:
    print(players[(len(cities) - 1) % 2])  
