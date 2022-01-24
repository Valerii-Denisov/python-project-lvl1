#!/usr/bin/env python
"""The main script of brain even game."""
from brain_games import engine
from brain_games.games import gcd


def main():
    """
    Run game.

    Using function of game_cycle.py and brain_gcd_logic.py
    """
    engine.start_game(gcd)


if __name__ == '__main__':
    main()
