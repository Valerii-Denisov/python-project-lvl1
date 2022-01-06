#!/usr/bin/env python
"""The main script of brain even game."""
from brain_games import game_cycle
from brain_games.games_logic import brain_prime_logic


def main():
    """
    Run game.

    Using function of game_cycle.py and brain_prime_logic.py
    """
    user_name = game_cycle.greet()
    brain_prime_logic.printing_rule()
    game_cycle.game_cycle(brain_prime_logic, user_name)


if __name__ == '__main__':
    main()
