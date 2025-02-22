import random

emoji_dict = {
    "r": "✊",
    "p": "✋",
    "s": "✌"
}

rps = ['r', 'p', 's']

while True:
    com = random.choice(rps)
    human = input("Rock, Paper or Scissor? (r/p/s): ").lower()
    if human not in rps:
        print('Invalid Choice')
    else:
        print(f"You chose {emoji_dict[human]}")
        print(f"Computer chose {emoji_dict[com]}")
        
        if com == human:
            print("Tie!!")
        elif (
            (human == 'r' and com == 's') or
            (human == 'p' and com == 'r') or
            (human == 's' and com == 'p')):
            print("You Won!!!")
        else:
            print("You Lost!!!")
        prompt = input("Continue? (y/n): ").lower()
        if prompt == 'n':
            break