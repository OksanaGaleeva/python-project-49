from brain_games.scripts.engine import engine
from brain_games.scripts.games.game_brain_calc import calc_game


def main():
    engine(calc_game, 'What is the result of the expression?')