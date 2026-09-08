from brain_games.scripts.engine import engine
from brain_games.scripts.games.game_brain_progression import progression_game


def main():
    engine(progression_game, 'What number is missing in the progression?')