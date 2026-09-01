import prompt
import random

def main():
    print('Welcome to the Brain Games!')
    name_user = welcome_user()
    print('What is the result of the expression?')
    engine(name_user)


def engine(name_user):
    number_answer = number()
    if number_answer == True:
        x = 0
        while number_answer == True and x < 2:
            x = x + 1
            number_answer = number()
        print("Congratulations, " + name_user + "!")
        return
    print("Let's try again, " + name_user + "!")


def number():
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


def welcome_user():
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    return name