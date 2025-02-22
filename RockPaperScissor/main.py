import random

emoji_dict = {
    "r": "✊",
    "p": "✋",
    "s": "✌"
}

choices = ['r', 'p', 's']

def get_user_choice():
    user_choice = input("Rock, Paper or Scissor? (r/p/s): ").lower()
    if user_choice in choices:
        return user_choice
    else:
        print("Invalid Choice")
        
def get_computer_choice():
    computer_choice = random.choice(choices)
    return computer_choice


def display_choices(user_choice, computer_choice):
    print(f"You chose {emoji_dict[user_choice]}")
    print(f"Computer chose {emoji_dict[computer_choice]}")

def determine_winner(user_choice, computer_choice):
    if computer_choice == user_choice:
            print("Tie!!")
    elif (
        (user_choice == 'r' and computer_choice == 's') or
        (user_choice == 'p' and computer_choice == 'r') or
        (user_choice == 's' and computer_choice == 'p')):
        print("You Won!!!")
    else:
        print("You Lost!!!")

def play_game():
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        display_choices(user_choice, computer_choice)
        
        determine_winner(user_choice,computer_choice)
        prompt = input("Continue? (y/n): ").lower()
        if prompt == 'n':
            return

play_game()