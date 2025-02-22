import random

emoji_dict = {
    "rock": "✊",
    "paper": "✋",
    "scissors": "✌"
}

rps = ['r', 'p', 's']

while True:
    com = random.randint(0, 2)
    com = rps[com]
    human = input("Rock, Paper or Scissor? (r/p/s): ").lower()

    if human not in rps:
        print('Invalid Choice')
    else:
        if human == 'r':
            print(f"Your Choice {emoji_dict['rock']}")
            if com == 'r':
                print(f"Computer Choice {emoji_dict['rock']}")
                print("Tie!!!")
            elif com == 'p':
                print(f"Computer Choice {emoji_dict['paper']}")
                print("You Won!!!")
            else:
                print(f"Computer Choice {emoji_dict['scissors']}")
                print("You Lost!!!")
            
        elif human == 'p':
            print(f"Your Choice {emoji_dict['paper']}")
            if com == 'r':
                print(f"Computer Choice {emoji_dict['rock']}")
                print("You Won!!!")
            elif com == 'p':
                print(f"Computer Choice {emoji_dict['paper']}")
                print("Tie!!!")
            else:
                print(f"Computer Choice {emoji_dict['scissors']}")
                print("You Lost!!!")
        
        else:
            print(f"Your Choice {emoji_dict['scissors']}")
            if com == 'r':
                print(f"Computer Choice {emoji_dict['rock']}")
                print("You Lost!!!")
            elif com == 'p':
                print(f"Computer Choice {emoji_dict['paper']}")
                print("You Won!!!")
            else:
                print(f"Computer Choice {emoji_dict['scissors']}")
                print("Tie!!!")
        prompt = input("Continue? (y/n): ").lower()
        if prompt == 'n':
            break