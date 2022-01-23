import numpy as np
import time


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
