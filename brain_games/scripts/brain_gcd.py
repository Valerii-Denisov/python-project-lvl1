#!/usr/bin/env python
"""The main script of brain even game."""
from brain_games import game_cycle
from brain_games.games import brain_gcd_logic


def main():
    """
    Run game.

    Using function of game_cycle.py and brain_gcd_logic.py
    """
    game_cycle.game_cycle(brain_gcd_logic)


if __name__ == '__main__':
    main()
