"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    _dict = {}

    for item in items:
        if not item in _dict:
            _dict[item] = 0
        _dict[item] += 1

    return _dict
