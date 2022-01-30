"""The module contains the rules of the game and its functions."""
from random import randint

RULES = 'Find the greatest common divisor of given numbers.'
BOUNDS = (0, 100)


def get_gcd(number_one, number_two):
    """
    Calculate the greatest common divisor.

    Parameters:
        number_one: int,
        number_two: int

    Returns:
        greatest common divisor.
    """
    while number_one != 0 and number_two != 0:
        if number_one > number_two:
            number_one %= number_two
        else:
            number_two %= number_one
    return number_one + number_two


def get_game_data():
    """
    Generate question number and return correct answer.

    Returns:
            cor_answer,
            question_string.
    """
    num1 = randint(*BOUNDS)
    num2 = randint(*BOUNDS)
    quest_number = get_gcd(num1, num2)
    return str(quest_number), '{0} {1}'.format(num1, num2)
