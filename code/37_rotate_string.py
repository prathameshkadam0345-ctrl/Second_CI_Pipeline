# Program 37: Rotate a String by K Positions

def rotate_string(string, k):
    if not string:
        return string

    k = k % len(string)

    return string[-k:] + string[:-k] if k else string