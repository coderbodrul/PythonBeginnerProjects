import random
ans = random.randint(1, 100)

while True:
    try:
        num = int(input('Guess the number between 1 and 100: '))
        if 1 <= num <= 100:
            if num == ans:
                print('Congratulations!!!')
                break
            elif num < ans:
                print('Low')
            else:
                print('High')
        else:
            print('Enter a number between 1 and 100')
    except ValueError:
        print('Please enter a valid number.')