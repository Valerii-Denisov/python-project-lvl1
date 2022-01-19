#!/usr/bin/env python
"""The main script of brain even game."""
from brain_games import engine
from brain_games.games import brain_even_logic


def main():
    """
    Run game.

    Using function of game_cycle.py and brain_even_logic.py
    """
    engine.game_cycle(brain_even_logic)


if __name__ == '__main__':
    main()
