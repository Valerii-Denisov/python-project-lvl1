"""The module contains the rules of the game and its functions."""
from random import choice, randint

RULE = 'What number is missing in the progression?'


def correct_answer():
    """
    Generate question number and return correct answer.

    Returns:
            cor_answer,
            question_string.
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
    return cor_answer, ' '.join(array)
