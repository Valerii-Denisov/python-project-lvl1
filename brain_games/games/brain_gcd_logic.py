"""The module contains the rules of the game and its functions."""
from random import randint

RULE = 'Find the greatest common divisor of given numbers.'


def correct_answer():
    """
    Generate question number and return correct answer.

    Returns:
            cor_answer,
            question_string.
    """
    bound = (0, 100)
    num1 = randint(bound[0], bound[1])
    num2 = randint(bound[0], bound[1])
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 %= num2
        else:
            num2 %= num1
    return str(num1 + num2), '{0} {1}'.format(num1, num2)
