from dice_game import dicePlaying

while True:
    choice = input('Roll the dice (y / n): ').lower()
    if choice == 'y':
        times = int(input('How many times do you want to play? : '))
        if times <= 0:
            print(f'You can\'t play {times} times')
        else:
            dicePlaying(times)
    elif choice == 'n':
        print('Thank You!')
        break
    else:
        print('Invalid Choice')