import prompt

def engine(game_func, welcome_answer):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print(welcome_answer)
    number_answer = game_func()
    if number_answer == True:
        x = 0
        while number_answer == True and x < 2:
            x = x + 1
            number_answer = game_func()
        if number_answer == True:
            print("Congratulations, " + name + "!")
            return
    print("Let's try again, " + name + "!")