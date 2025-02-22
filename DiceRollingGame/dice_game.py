import random

def dicePlaying(times):
    while times:
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f'({die1}, {die2})')
        times -= 1