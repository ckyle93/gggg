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
    translator = {}
    for i in range(0, len(text), 2):
        translator[text[i+1]] = text[i]
    return translator

""" Reads in some text, parses it into
    words, then letters until it can find
    a corresponding match in the dictionary.
"""
def translate_text(text, translator):
    words = re.split('\n+| ', text)
    translation = ''
    for word in words:
        for partial_letter in word:
            letter = ''
            letter += partial_letter
            for k, v in translator.items():
                if k == letter:
                    translation += v
                    letter = ''
                    break
    return translation

testdict = {1 : 'this', 2 : 'is', 3 : 'a', 4 : 'test'}
print(translate_text('12 34 44 21', testdict))
print(read_key('test'))
