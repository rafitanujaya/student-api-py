import random


def random_id(length):
    return "".join(str(random.randint(0, 9)) for _ in range(length))