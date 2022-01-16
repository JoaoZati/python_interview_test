"""
7) Think that you have an unlimited number of carrots, but a limited number of carrot
types. Also, you have one bag that can hold a limited weight. Each type of carrot has a
weight and a price. Write a function that takes carrotTypes and capacity and return the
maximum value the bag can hold.
Example:
carrotTypes = [{kg: 5, price: 100}, {kg: 7, price: 150}, {kg: 3, price: 70}]
capacity = 36 //kg
getMaxValue(carrotTypes, capacity)

>>> carrotTypes = [{'kg': 5, 'price': 100}, {'kg': 7, 'price': 150}, {'kg': 3, 'price': 70}]
>>> capacity = 36
>>> getMaxValue(carrotTypes, capacity)
840
"""

import math


def getMaxValue(carrotTypes, capacity):
    max_value = 0
    for i, carrot in enumerate(carrotTypes):
        carrot_kg = carrot['kg']
        carrot_price = carrot['price']
        floor = math.floor(capacity / carrot_kg)

        missing = capacity - floor * carrot_kg
        max_missing = getMaxValue(carrotTypes[:i] + carrotTypes[i + 1:], missing)

        new_value = floor * carrot_price
        max_value = max(max_value, new_value + max_missing)

    return max_value
