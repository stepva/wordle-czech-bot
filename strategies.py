import numpy as np

from __init__ import DEBUG
from methods import check_guess, pick_guess, pick_guess_wo_altering


def strategy_0(main_word, guesses, letters, known, includes, good, wrong, uniques):
    """
    Žádná special pravidla
    """

    i = 0
    while i < 7:
        i += 1

        guess = pick_guess(guesses, letters=letters, known=known, includes=includes)

        if check_guess(main_word, guess, letters, known, includes):
            break

    if i == 7:
        wrong.append(main_word)
    else:
        good = np.append(good, i)

    return good, wrong


def strategy_1(main_word, guesses, letters, known, includes, good, wrong, uniques):
    """
    První guess z uniques, druhý guess z uniques jen s možnými písmeny, další normálně
    """

    i = 0
    while i < 7:
        i += 1
        if DEBUG:
            print("guess: ", i, guess)

        if i == 1 or i == 2:
            guess = pick_guess_wo_altering(uniques, letters=letters)
        else:
            guess = pick_guess(guesses, letters=letters, known=known, includes=includes)

        if check_guess(main_word, guess, letters, known, includes):
            break

    if i == 7:
        if DEBUG:
            print("NEUHODL!", main_word)
        wrong.append(main_word)
    else:
        if DEBUG:
            print("UHODL!", main_word, i)
        good = np.append(good, i)

    return good, wrong


def strategy_2(main_word, guesses, letters, known, includes, good, wrong, uniques):
    """
    První guess z uniques, další normálně
    """

    i = 0
    while i < 7:
        i += 1
        if DEBUG:
            print("guess: ", i, guess)

        if i == 1:
            guess = pick_guess_wo_altering(uniques, letters=letters)
        else:
            guess = pick_guess(guesses, letters=letters, known=known, includes=includes)

        if check_guess(main_word, guess, letters, known, includes):
            break

    if i == 7:
        if DEBUG:
            print("NEUHODL!", main_word)
        wrong.append(main_word)
    else:
        if DEBUG:
            print("UHODL!", main_word, i)
        good = np.append(good, i)

    return good, wrong
