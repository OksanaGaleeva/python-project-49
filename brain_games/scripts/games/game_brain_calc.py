import prompt
import random

def calc_game():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    y = random.randint(1, 3)
    if y == 1:
        c = "+"
    elif y == 2:
        c = "-"
    else:
        c = "*"
    print("Question: " + str(a) + str(c) + str(b))
    match c:
        case "+":
            right_answer = a + b
        case "-":
            right_answer = a - b
        case "*":
            right_answer = a * b

    answer = prompt.string('Your answer: ')

    if answer == str(right_answer):
        print('Correct!')
        return True
    else:
        print(str(answer) + ' is wrong answer ;(. Correct answer was ' + str(right_answer) + '.')
        return False