"""
1) Write a python function that finds the duplicate items in any given array.

>>> duplicate_items_array([1, 2, 3, 4, 5, 2, 3])
[2, 3]
>>> duplicate_items_array([1, 2, 3])
[]
>>> duplicate_items_array([1,1,1,2,3,3,'hy', 'hy'])
[1, 1, 3, 'hy']

Note: I can find its position on the given array using enumarate
>>> enumerate_duplicated_itens([1, 2, 3, 4, 5, 2, 3])
{5: 2, 6: 3}
>>> enumerate_duplicated_itens([1,1,1,2,3,3,'hy', 'hy'])
{1: 1, 2: 1, 5: 3, 7: 'hy'}
"""


def duplicate_items_array(array):
    list_duplicated = []

    empty_set = set()

    for item in array:
        if item in empty_set:
            list_duplicated.append(item)

        empty_set.add(item)

    return list_duplicated


def duplicate_items_array(array):
    list_duplicated = []

    empty_set = set()

    for item in array:
        if item in empty_set:
            list_duplicated.append(item)

        empty_set.add(item)

    return list_duplicated


def enumerate_duplicated_itens(array):
    dict_duplicated = {}

    empty_set = set()

    for i, item in enumerate(array):
        if item in empty_set:
            dict_duplicated[i] = item

        empty_set.add(item)

    return dict_duplicated
