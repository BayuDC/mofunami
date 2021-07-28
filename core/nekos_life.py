import nekos

from random import choice
from functools import reduce
from data.nekos_life import nekos_data


class NekosLifeCore:
    def get_categories(self):
        return reduce(lambda result, category: f'{result}`{self.get_category_aliases(category)}` ', nekos_data.categories, '')

    def get_category(self):
        return self.get_category_aliases(choice(nekos_data.categories))

    def get_category_aliases(self, category):
        aliases_keys = list(nekos_data.aliases.keys())
        aliases_values = list(nekos_data.aliases.values())

        if category in aliases_values:
            return aliases_keys[aliases_values.index(category)]

        return category

    def get_img(self, category):
        if category in nekos_data.aliases:
            category = nekos_data.aliases[category]
        elif category not in nekos_data.categories:
            return None

        return nekos.img(category)


nekos_core = NekosLifeCore()
