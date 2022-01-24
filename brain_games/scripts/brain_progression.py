#!/usr/bin/env python
"""The main script of brain even game."""
from brain_games import engine
from brain_games.games import progression


def main():
    """
    Run game.

    Using function of game_cycle.py and brain_progression_logic.py
    """
    engine.start_game(progression)


if __name__ == '__main__':
    main()
