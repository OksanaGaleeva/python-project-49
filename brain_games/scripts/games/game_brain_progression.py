import prompt
import random

def progression_game():
    length = random.randint(5, 10)
    progression = []
    start = random.randint(0, 15)
    empty_element = random.randint(0, length - 1)
    counter = 0
    step = random.randint(1, 10)

    progression.append(str(start))
    for i in range (2, length):
        start = start + step
        progression.append(str(start))

    progression[empty_element] = '  '
    output = " ".join(progression)
    print(output)
    answer = prompt.string('Your answer: ')
    right_answer = str(step)
    
    if answer == right_answer:
        print('Correct!')
        return True
    else:
        print(answer + ' is wrong answer ;(. Correct answer was ' + right_answer + '.')
        return False