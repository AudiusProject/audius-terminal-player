import random


def get_random_element_from_list(list):
    return random.choice(list)


def numerize(num):
    if num < 10 ** 3:
        return f"{num:>.0f} "
    if num < 10 ** 6:
        return f"{num/10**3:.1f}k"
    if num < 10 ** 9:
        return f"{num/10**6:.1f}M"
    return num
