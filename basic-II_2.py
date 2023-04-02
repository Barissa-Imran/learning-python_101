"""
creates all possible strings using the letters making sure each character is used only once
"""


import random

chars = ['a', 'e', 'i', 'o', 'l']

random.shuffle(chars)

print(''.join(chars))
