#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence == "":
        first_char = None
    else:
        first_char = sentence[0]
    return len(sentence), first_char
