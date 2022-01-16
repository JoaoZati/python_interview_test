"""
4) Write an efficient method that tells us whether or not an input string brackets ("{", "}",
"(", ")", "[", "]") opened and closed properly. Example: “{[]}” => true, “{(])}” => false,
“{([)]}” => false

>>> properly_brackets("{[]}")
True
>>> properly_brackets("{[Hello Word],[Other Word]}")
True
>>> properly_brackets("[(){}")
False
>>> properly_brackets("{(])}")
False
>>> properly_brackets("{([)]}")
False
"""


def properly_brackets(string):
    if not isinstance(string, str):
        raise ValueError('The input must be a string')

    brackets_open = {'{', '(', '['}
    brackets_close = {'}', ')', ']'}

    dict_brackets = {
        '{': '}',
        '(': ')',
        '[': ']',
    }

    open_bracket = ''
    for letter in string:
        if letter in brackets_open:
            open_bracket += letter
            continue

        if letter in brackets_close:
            if letter == dict_brackets[open_bracket[-1]]:
                open_bracket = open_bracket[:-1]
                continue
            return False

    if open_bracket:
        return False

    return True
