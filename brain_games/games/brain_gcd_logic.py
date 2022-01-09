"""The module contains the rules of the game and its functions."""
from random import randint


def printing_rule():
    """Print game rules."""
    print('Find the greatest common divisor of given numbers.')


def correct_answer():
    """
    Generate question number and return correct answer.

    Returns:
            cor_answer.
    """
    bound = [0, 100]
    num1 = randint(bound[0], bound[1])
    num2 = randint(bound[0], bound[1])
    print('Question: {0} {1}'.format(num1, num2))
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 %= num2
        else:
            num2 %= num1
    return str(num1 + num2)


def user_answer():
    """
    Asks the user for his answer and return his.

    Returns:
            u_answer.
    """
    u_answer = input('Your answer: ')
    return u_answer
