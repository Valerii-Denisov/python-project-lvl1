#!/usr/bin/env python
"""The main script of brain even game."""
from brain_games import engine
from brain_games.games import brain_calc_logic


def main():
    """
    Run game.

    Using function of engine.py and calc.py
    """
    engine.start_game_cycle(brain_calc_logic)


if __name__ == '__main__':
    main()
