"""Helper functions
"""

def convert_index_to_character(keys, index):
    return keys[index]

def convert_character_to_index(keys, char):
    return keys.index(char)

def wrap_round_index(keys, index):
    return index % len(keys)
