"""The module contains the rules of the game and its functions."""
from random import choice, randint

RULES = 'What number is missing in the progression?'
DIFFERENCE_BORDER = (0, 100)
PROGRESSION_LENGTH_BORDER = (5, 10)
INITIAL_TERM_BORDER = (0, 1000)


def get_progression(initial_term, difference, max_array_length):
    """
    Generate progression.

    Parameters:
        difference: tuple
        initial_term: tuple
        max_array_length: tuple

    Returns:
            progression.
    """
    progression_length = 0
    progression = []
    while progression_length < max_array_length:
        progression.append(str(initial_term))
        initial_term += difference
        progression_length += 1
    return progression


def stringify_progression(progression, hidden_term_index):
    """
    Take the progression and index of the hidden element.

    Generate and return the question string.

    Parameters:
        progression: list,
        hidden_term_index: int

    Returns:
            string.
    """
    question_progression = progression[:]
    question_progression[hidden_term_index] = '..'
    return ' '.join(question_progression)


def get_game_data():
    """
    Generate question number and return correct answer.

    Returns:
            cor_answer,
            question_string.
    """
    initial_term = randint(*INITIAL_TERM_BORDER)
    difference = randint(*DIFFERENCE_BORDER)
    max_array_length = randint(*PROGRESSION_LENGTH_BORDER)
    progression = get_progression(initial_term, difference, max_array_length)
    hidden_term_index = choice(range(max_array_length))
    return (
        progression[hidden_term_index],
        stringify_progression(progression, hidden_term_index),
    )
