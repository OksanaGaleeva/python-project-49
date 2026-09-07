import prompt
import random

def gcd_game():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    print(str(a) + ' ' + str(b))
    answer = prompt.string('Your answer: ')

    while b != 0:
        x = abs(b)
        b = abs(a) % abs(b)
        a = x
    right_answer = str(a)
    

    if answer == right_answer:
        print('Correct!')
        return True
    else:
        print(answer + ' is wrong answer ;(. Correct answer was ' + right_answer + '.')
        return False