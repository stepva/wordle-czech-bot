import random
import re

from __init__ import DEBUG


def pick_guess(guesses, lts, known=None, includes=None):
    if DEBUG:
        print("entering pick_guess: ", len(guesses), known, includes)

    guesses[:] = [g for g in guesses if all(l in lts for l in g)]

    if known:
        r = re.compile("".join(known.values()))
        guesses[:] = list(filter(r.match, guesses))

    if includes:
        guesses[:] = [
            w
            for w in guesses
            if all(
                len(re.findall(l, w)) == includes["exact"][l]
                for l in includes["exact"].keys()
            )
        ]
        guesses[:] = [
            w
            for w in guesses
            if all(
                len(re.findall(l, w)) >= includes["at_least"][l]
                for l in includes["at_least"].keys()
            )
        ]

    choice = random.choice(guesses)

    if DEBUG:
        print("exiting pick_guess: ", len(guesses), choice)
    return choice


def pick_guess_wo_altering(guesses, lts):
    subset = [g for g in guesses if all(l in lts for l in g)]
    return random.choice(subset)


def check_guess(word, guess, letters, known, includes):
    if word == guess:
        return True

    nots = []
    for letter in guess:
        if letter not in word:
            nots.append(letter)
        if letter in word:
            inds_word = [m.start() for m in re.finditer(letter, word)]
            inds_guess = [m.start() for m in re.finditer(letter, guess)]
            correct = list(set(inds_word) & set(inds_guess))

            for i in correct:
                known[i] = letter

            if len(inds_word) <= len(inds_guess):
                includes["exact"][letter] = len(inds_word)
            elif len(inds_word) > len(inds_guess):
                includes["at_least"][letter] = len(inds_guess)

            for i in [x for x in inds_guess if x not in correct]:
                if not len(known[i]) == 1:
                    known[i] = known[i][:-1] + letter + "]"

    for l in list(set(nots)):
        letters.remove(l)
    return False
