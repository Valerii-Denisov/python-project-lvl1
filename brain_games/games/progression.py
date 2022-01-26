"""The module contains the rules of the game and its functions."""
from random import choice, randint

RULES = 'What number is missing in the progression?'
DIFFERENCE_BORDER = (0, 100)
PROGRESSION_LENGTH_BORDER = (5, 10)
INITIAL_TERM_BORDER = (0, 1000)


def get_array():
    """
    Generate array.

    Returns:
            array.
    """
    array_length = 0
    array = []
    initial_term = randint(INITIAL_TERM_BORDER[0], INITIAL_TERM_BORDER[1])
    difference = randint(DIFFERENCE_BORDER[0], DIFFERENCE_BORDER[1])
    max_array_length = randint(
        PROGRESSION_LENGTH_BORDER[0],
        PROGRESSION_LENGTH_BORDER[1],
    )
    while array_length < max_array_length:
        array.append(str(initial_term))
        initial_term += difference
        array_length += 1
    return array


def get_progression_string(array):
    """
    Turn a progression into a string.

    Parameters:
        array: list

    Returns:
            string.
    """
    return ' '.join(array)


def get_game_data():
    """
    Generate question number and return correct answer.

    Returns:
            cor_answer,
            question_string.
    """
    array = get_array()
    cor_answer = choice(array)
    array[array.index(cor_answer)] = '..'
    return cor_answer, get_progression_string(array)
