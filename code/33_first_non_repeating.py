# Program 33: First Non-Repeating Character

def first_non_repeating_char(string):
    for char in string:
        if string.count(char) == 1:
            return char

    return None