numberofticket = 0
while True:
    numberofticket += 1
    ticket = input()
    if len(ticket) % 2 == 0 and \
       sum(map(int, ticket[:len(ticket)//2])) == sum(map(int, ticket[len(ticket)//2:])):
        print(numberofticket)
        break
