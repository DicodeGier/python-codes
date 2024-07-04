names = []
amounts = []
new_amount = 1
while int(new_amount) > 0:
    names.append(input("give the name "))
    new_amount = int(input("give the amount "))
    amounts.append(new_amount)

def nameOfBestCustomer(names, amounts, topN):
    counter = 1
    winners = []
    while counter <= topN:
        max_amount = max(amounts)
        index = amounts.index(max_amount)
        if max_amount != 0:
            winners.append(names[index])
        names.pop(index)
        amounts.pop(index)
        counter += 1
    return winners
        

print(nameOfBestCustomer(names, amounts, 3))

