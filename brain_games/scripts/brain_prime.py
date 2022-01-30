#!/usr/bin/env python
"""The main script of brain even game."""
from brain_games import engine
from brain_games.games import prime


def main():
    """
    Run game.

    Using function of game_cycle.py and brain_prime_logic.py
    """
    engine.run_game(prime)


if __name__ == '__main__':
    main()
