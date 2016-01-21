# By Chris Kyle
# Written for the reddit/r/DailyProgrammer challenge #245

import re

""" Reads in a file and creates a dictionary
    of keys to values, which assumes the in file
    is formatted as "value Key value Key ..."
"""
def read_key(infile):
    f = open(infile, 'r')
    text = re.split('\n+| ', f.read())
    text.remove('')
    key = {}
    for i in range(0, len(text), 2):
        key[text[i+1]] = text[i]
    return translator

""" Reads in some text, parses it into
    words, then letters until it can find
    a corresponding match in the dictionary.
"""
def translate_text(text, translator):
    words = re.split('\n+| ', text)
    for word in words:
        for partial_letter in word:
            letter += partial_letter
            for k, v in key.items():
                if k == letter:
                    translation += v


print(read_key('test'))
