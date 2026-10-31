# Program 31: Check Whether a Sentence Is a Pangram

def is_pangram(sentence):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    letters = set(sentence.lower())

    return alphabet.issubset(letters)