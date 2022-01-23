import numpy as np

from __init__ import DEBUG
from methods import check_guess, pick_guess, pick_guess_wo_altering


def strategy_1(main_word, guesses, letters, known, includes, good, wrong, uniques):
    """
    První guess z uniques, druhý guess z uniques jen s možnými písmeny, další normálně
    """
    guess = pick_guess_wo_altering(uniques, lts=letters)

    i = 1
    while i < 7:
        if DEBUG:
            print("guess: ", i, guess)
        if check_guess(main_word, guess, letters, known, includes):
            break

        if i == 1:
            guess = pick_guess_wo_altering(uniques, lts=letters)
        else:
            guess = pick_guess(guesses, lts=letters, known=known, includes=includes)

        i += 1
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
    guess = pick_guess_wo_altering(uniques, lts=letters)

    i = 1
    while i < 7:
        if DEBUG:
            print("guess: ", i, guess)
        if check_guess(main_word, guess, letters, known, includes):
            break

        guess = pick_guess(guesses, lts=letters, known=known, includes=includes)

        i += 1
    if i == 7:
        if DEBUG:
            print("NEUHODL!", main_word)
        wrong.append(main_word)
    else:
        if DEBUG:
            print("UHDODL!", main_word, i)
        good = np.append(good, i)

    return good, wrong
