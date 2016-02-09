# By Chris Kyle
# Written for the reddit/r/DailyProgrammer challenge #245

import re

""" Reads in a file and creates a dictionary
    of keys to values, which assumes the in file
    is formatted as "value Key value Key ..."
"""
def read_key(dictionary):
    text = re.split('\n+| ', dictionary)
    text.remove('')
    translator = {}
    for i in range(0, len(text), 2):
        translator[text[i+1]] = text[i]
    return translator

""" Reads in some text, parses it into
    words, then letters until it can find
    a corresponding match in the dictionary.
"""
def translate_text(foreign_text, translator):
    words = re.split('\n+| ', foreign_text)
    translation = ''
    for word in words:
        letter = ''
        for partial_letter in word:
            if partial_letter != 'g' and partial_letter != 'G':
                translation += partial_letter
                continue
            letter += partial_letter
            for k, v in translator.items():
                if k == letter:
                    translation += v
                    letter = ''
                    break
        translation += ' '
    return translation

file_name = input('Enter filename containing a key and a message to decode: ')
f = open(file_name, 'r')
dictionary = f.readline()
foreign_text = f.readline()
print(translate_text(foreign_text, read_key(dictionary)))
