import random

strat_1 = 0
strat_2 = 0
simulations = 0

while simulations <= 10000:
    player_choice = random.randint(1,3)
    correct_door = random.randint(1,3)
    if player_choice == correct_door == 1:
        shown_door = random.randint(2,3)
    if player_choice == correct_door == 2:
        shown_door = random.choice([1,3])
    if player_choice == correct_door == 3:
        shown_door = random.randint(1,2)

    door_choices = [1,2,3]
    if player_choice != correct_door:
        door_choices.pop(door_choices.index(correct_door))
        door_choices.pop(door_choices.index(player_choice))
        shown_door = random.choice(door_choices)

    door_choices = [1,2,3]
    altered_choice = door_choices.pop(door_choices.index(player_choice))
    altered_choice = door_choices.pop(door_choices.index(shown_door))
    altered_choice = random.choice(door_choices)
    if player_choice == correct_door:
        strat_1 += 1
        simulations += 1
    elif altered_choice == correct_door:
        strat_2 += 1
        simulations += 1

print(strat_1)
print(strat_2)