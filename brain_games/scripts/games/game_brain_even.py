import prompt
import random

def even_game():
    n = random.randint(1, 100)
    print(n)
    answer = prompt.string('Your answer: ')

    if n % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'

    if answer == right_answer:
        print('Correct!')
        return True
    else:
        print(answer + ' is wrong answer ;(. Correct answer was ' + right_answer + '.')
        return False