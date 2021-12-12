import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    ls = []
    for x in range(100):
        ls.append(random.randint(0,1))
    # Code that checks if there is a streak of 6 heads or tails in a row.
    streak = 0
    state = 0   # 0 for tails 1 for heads
    for x in ls:
        if x == state:
            streak += 1
            if streak == 6:
                numberOfStreaks += 1
                break
        else:
            state != state
            streak = 0
print('Chance of streak: %s%%' % (numberOfStreaks / 100))