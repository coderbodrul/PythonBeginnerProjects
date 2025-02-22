cnt = 0
def game(dict):
    global cnt
    while True:
        try:
            num = int(input(f"Guess the number between {dict['min']} and {dict['max']}: "))
            if dict['min'] <= num <= dict['max']:
                if num == dict['ans']:
                    print('Congratulations!!! You guessed the number')
                    print(f"Your score is = {cnt + 1}. Best Score is {dict['best_score']}") 
                    break
                elif num < dict['ans']:
                    print('Low')
                    cnt = cnt + 1
                else:
                    print('High')
                    cnt = cnt + 1
            else:
                print(f"Enter a number between {dict['min']} and {dict['max']}")

            if cnt == dict['limit']:
                print('Sorry. You crossed your attempt\'s limit')
                print(f"Your score is = {cnt}. Best Score is = {dict['best_score']}.")
                
        except ValueError:
            print('Please enter a valid number.')