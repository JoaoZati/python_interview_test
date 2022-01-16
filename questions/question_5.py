"""
5) A building has 100 floors. One of the floors is the highest floor an egg can be dropped
from without breaking. If an egg is dropped from above that floor, it will break. If it is
dropped from that floor or below, it will be completely undamaged and you can drop theegg again. Given two eggs, find the highest floor an egg can be dropped from without
breaking, with as few drops as possible on the worst-case scenario.
"""

import random


def highest_floor_egg():
    """
    Simulate a random floor that a egg can be drooped without break with randomly
    and calculate the number of drops needed to find it. It start drop on first level and going on until the first level
    egg breaks.

    :return: dict, keys: 'droops': number of drops to find highers floor, 'max_floor': number of floor.
    """
    max_floor = random.randint(1, 100)

    for i in list(range(1, 101)):
        if i > max_floor:
            print(f'Total Drops: {i}, Max floor without breack: {i - 1}')
            return {'drops': i, 'max_floor': i + 1}

    return None


if __name__ == '__main__':
    highest_floor_egg()
