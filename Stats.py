import random


def health():
    return random.randrange(100, 200)


def strength():
    return random.randrange(10, 15)


def defense():
    return random.randrange(5,10)


def gold():
    return random.randrange(100,150)


def exp():
    return 0


def level():
    level = 1
    return level