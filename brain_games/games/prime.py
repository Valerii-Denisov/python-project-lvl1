"""The module contains the rules of the game and its functions."""
from random import randint

RULES = "Answer 'yes' if the number is prime, otherwise answer 'no'."
BOUNDS = (0, 3571)


def is_prime(number):
    """
    Check whether a number is prime.

    Parameters:
        number: int

    Returns:
        True,
        False.
    """
    for divider in range(2, number // 2 + 1):
        if number % divider == 0:
            return False
    return True


def get_game_data():
    """
    Generate question number and return correct answer.

    Returns:
            cor_answer,
            question_string.
    """
    num = randint(*BOUNDS)
    cor_answer = 'yes' if is_prime(num) else 'no'
    return cor_answer, num
