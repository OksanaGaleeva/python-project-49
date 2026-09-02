import prompt
import random


def main():
    print('Welcome to the Brain Games!')
    name_user = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    number_answer = number()
    if number_answer == True:
        number_answer = number()
        if number_answer == True:
            number_answer = number()
            print("Congratulations, " + name_user + "!")
            return
    print("Let's try again, " + name_user + "!")


def number():
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


def welcome_user():
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    return name