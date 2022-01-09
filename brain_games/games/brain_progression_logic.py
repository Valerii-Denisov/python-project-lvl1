"""The module contains the rules of the game and its functions."""
from random import choice, randint


def printing_rule():
    """Print game rules."""
    print('What number is missing in the progression?')


def correct_answer():
    """
    Generate question number and return correct answer.

    Returns:
            cor_answer.
    """
    array_length = 0
    array = []
    element = randint(0, 1000)
    step = randint(0, 100)
    while array_length < randint(5, 10):
        array.append(str(element))
        element += step
        array_length += 1
    cor_answer = choice(array)
    array[array.index(cor_answer)] = '..'
    print('Question: {0}'.format(' '.join(array)))
    return cor_answer


def user_answer():
    """
    Asks the user for his answer and return his.

    Returns:
            u_answer.
    """
    u_answer = input('Your answer: ')
    return u_answer
