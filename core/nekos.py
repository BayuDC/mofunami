import nekos
import random
import functools

from data import nekos as nekos_data


def category_random() -> str:
    return category_aliases(random.choice(nekos_data.categories))


def category_summary() -> str:
    return functools.reduce(lambda result, category: f'{result}`{category_aliases(category)}` ', nekos_data.categories, '')


def category_aliases(category: str) -> str:
    if category in nekos_data.aliases_inverse:
        return nekos_data.aliases_inverse[category]

    return category


def img(category: str) -> str:
    if category in nekos_data.aliases:
        category = nekos_data.aliases[category]
    elif category not in nekos_data.categories:
        return None

    return nekos.img(category)
