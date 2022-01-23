import numpy as np
import time

LETTERS = [
    "ě",
    "š",
    "č",
    "ř",
    "ž",
    "ý",
    "á",
    "í",
    "é",
    "ů",
    "q",
    "w",
    "e",
    "r",
    "t",
    "y",
    "u",
    "i",
    "o",
    "p",
    "a",
    "s",
    "d",
    "f",
    "g",
    "h",
    "j",
    "k",
    "l",
    "z",
    "x",
    "c",
    "v",
    "b",
    "n",
    "m",
]
# LETTERS = list(set([l for w in GUESSES for l in w]))


def get_words(word_file):
    with open(word_file, "r") as f:
        words = f.readlines()
        words = [w[:-1] for w in words]
    return words


def results(good, wrong, n, start):
    runs = n + 1
    n_good = len(good)
    n_wrong = len(wrong)

    print(f"Results from {runs} runs:")
    print(f"{n_good} correct, {n_wrong} wrong, {round(n_good / runs * 100, 2)}%")
    print(f"{round(np.mean(good), 2)} average guesses per correct word")
    print("Time in seconds: ", round(time.time() - start, 2))
