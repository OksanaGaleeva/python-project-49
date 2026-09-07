from brain_games.scripts.engine import engine
from brain_games.scripts.games.game_brain_gcd import gcd_game


def main():
    engine(gcd_game, 'Find the greatest common divisor of given numbers.')