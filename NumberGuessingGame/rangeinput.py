import random
import math

def takingrange():
    while True:
        try:
            min, max = map(int, input('Enter the range of guessing num: ').split())
            dict = calculatingNecessaryTerms(min, max)
            return dict
        except ValueError:
            print('Enter a valid range.')
    

def calculatingNecessaryTerms(min, max):
    dict = {
    'min' : min,
    'max' : max,
    'ans' : random.randint(min, max),
    'best_score' : int(math.log2(max - min + 1)),
    'limit' : (max - min) // 3 + 2
    }
    
    return dict
