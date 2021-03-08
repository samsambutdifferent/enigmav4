"""Helper functions
"""

def convert_index_to_character(keys, index):
    return keys[index]

def convert_character_to_index(keys, char):
    return keys.index(char)

def wrap_round_index(keys, index):
    return index % len(keys)

def lengths_out_of_range(keys, max, min):
    for key in keys:
        if len(key) > max or len(key) < min:
            return True
        for check_key in keys:
            if len(key) != len(check_key):
                return True

    return False