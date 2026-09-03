from brain_games.scripts.engine import engine
from brain_games.scripts.games.game_brain_even import even_game


def main():
    engine(even_game, 'Answer "yes" if the number is even, otherwise answer "no".')