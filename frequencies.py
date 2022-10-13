"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    _dict = {}

    for item in items:
        item = str(item)
        if not item in _dict:
            _dict[item] = 0
        _dict[item] += 1

    return _dict

print(frequencies([100, 'Hello', '100', '100', 100]))