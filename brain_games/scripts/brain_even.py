#!/usr/bin/env python
"""The main script of brain even game."""
from brain_games import game_cycle
from brain_games.games import brain_even_logic


def main():
    """
    Run game.

    Using function of game_cycle.py and brain_even_logic.py
    """
    game_cycle.game_cycle(brain_even_logic)


if __name__ == '__main__':
    main()
