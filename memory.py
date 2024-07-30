import random
import numpy as np
import matplotlib.pyplot as plt

def memory(num_pairs):
    """memory function calculates the (optimal?) number of turns needed to solve the game 'memory'.
    Assumption made is perfect memory (i.e. once a 'tile' has been turned, you will always remember what
    was beneath it). Game is solved by turning the first unturned 'tile' and choosing the second one if it has
    already been turned (remember perfect memory) or also turning the next 'tile' if the first tile was the first
    of the pair.

    Args:
        num_pairs (int): number of pairs in the game. Code will generate the random sequence of 'tiles'.

    Returns:
        turns (int): number of turns needed to solve the game.
    """
    all_numbers = list(range(1,num_pairs+1))
    all_numbers.extend(all_numbers)
    random.shuffle(all_numbers)
    print(all_numbers)

    seen_numbers = []
    index = 0
    turns = 0
    while len(all_numbers) > 0:
        first_choice = all_numbers[index]
        if first_choice in seen_numbers:
            second_choice_index = all_numbers.index(first_choice)
            all_numbers.pop(index)
            all_numbers.pop(second_choice_index)
            index = np.max([0, index - 1])
            index = np.min([index, len(all_numbers) - 1])
            turns += 1
        else:
            seen_numbers.append(first_choice)
            second_choice = all_numbers[index+1]
            if first_choice == second_choice:
                all_numbers.pop(index)
                all_numbers.pop(all_numbers.index(second_choice))
                index = np.min([index, len(all_numbers) - 1])
                turns += 1
            else:
                seen_numbers.append(second_choice)
                index = index + 2
                index = np.min([index, len(all_numbers) - 1])
                turns += 1

    return turns

if __name__ == "__main__":
    max_pairs = 10
    max_sim = 1000
    average_turns = []
    for i in range(2,max_pairs+1):
        total_turns = 0
        for j in range(max_sim):
            total_turns += memory(i)
        average_turns.append(total_turns/max_sim)

    x = np.array(range(2,max_pairs+1))
    y = np.array(average_turns)
    slope, intercept = np.polyfit(x, y, 1)
    regression_line = slope * x + intercept

    plt.scatter(x, y)
    plt.plot(x, regression_line, color='red')
    plt.xlabel('Number of pairs')
    plt.ylabel('Average turns')
    plt.title('Memory game')
    plt.grid()
    plt.savefig('memory_game.png')

    print(slope,intercept)