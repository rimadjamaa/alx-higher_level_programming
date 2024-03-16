#!/usr/bin/python3
def multiple_returns(sentence):
    # If the sentence is empty, return (0, None)
    if len(sentence) == 0:
        return (0, None)
    # first character
    return (len(sentence), sentence[0])
