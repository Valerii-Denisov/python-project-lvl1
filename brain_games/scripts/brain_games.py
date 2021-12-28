#!/usr/bin/env python
"""The main script of the project."""
from brain_games import cli


def main():
    """Display a greeting."""
    print('Welcome to the Brain Games!')
    cli.welcome_user()


if __name__ == '__main__':
    main()
