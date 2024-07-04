import random
total_results = []
counter = 0

jeroen_wins = 0
gerard_wins = 0
rene_wins = 0

simulations = 0

while simulations <= 100000:
    coin_toss = random.randint(0,1)
    counter += 1
    total_results.append(coin_toss)
    if counter == 1:
        continue
    for i in range (1, len(total_results)):
        if total_results[i] == 0 and total_results[i-1] == 0 and counter % 2 == 0:
            print(str(simulations) + ': ' + str(total_results) + ' ' + 'Jeroen wins')
            counter = 0
            jeroen_wins += 1
            total_results = []
            simulations += 1
    for j in range (1, len(total_results)):
        if total_results[j] == 1 and total_results[j-1] == 1 and counter % 2 == 0:
            print(str(simulations) + ': ' + str(total_results) + ' ' + 'Gerard wins')
            counter = 0
            gerard_wins += 1
            total_results = []
            simulations += 1
    if counter % 2 == 1:
        for k in range (1, len(total_results)):
            if (total_results[k] == 0 and total_results[k-1] == 0) or (total_results[k] == 1 and total_results[k-1] == 1):
                print(str(simulations) + ': ' + str(total_results) + ' ' +'Rene wins')
                counter = 0
                total_results = []
                rene_wins += 1
                simulations += 1

print('Jeroen wins ' + str(jeroen_wins) + ' times')
print('Gerard wins ' + str(gerard_wins) + ' times')
print('rene wins ' + str(rene_wins) + ' times')