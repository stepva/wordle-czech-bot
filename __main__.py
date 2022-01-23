import time
import random
import numpy as np

from strategies import strategy_1, strategy_2
from __init__ import DEBUG
from utils import get_words, results, LETTERS

# words.txt = možná slova jako tajenka (4 172 slov)
# guesses.txt = možná slova jako validní guess (21 923 slov)
# uniques.txt = slova s pěti různými písmeny (17 546 slov)

WORDS = get_words("words/words.txt")
GUESSES = get_words("words/guesses.txt")
UNIQUES = get_words("words/uniques.txt")


def main():
    start = time.time()

    good = np.array([])
    wrong = []

    for n in range(1000):
        if DEBUG:
            print("##############################################")

        guesses = GUESSES[:]
        letters = LETTERS[:]
        uniques = UNIQUES[:]
        known = {0: "[^.]", 1: "[^.]", 2: "[^.]", 3: "[^.]", 4: "[^.]"}
        includes = {"exact": {}, "at_least": {}}

        main_word = random.choice(WORDS)
        if DEBUG:
            print("word: ", main_word)

        good, wrong = strategy_1(
            main_word, guesses, letters, known, includes, good, wrong, uniques
        )

    results(good, wrong, n, start)


if __name__ == "__main__":
    main()
