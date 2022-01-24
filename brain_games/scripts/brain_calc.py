#!/usr/bin/env python
"""The main script of brain even game."""
from brain_games import engine
from brain_games.games import calc


def main():
    """
    Run game.

    Using function of engine.py and calc.py
    """
    engine.start_game(calc)


if __name__ == '__main__':
    main()
