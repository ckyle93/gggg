# By Chris Kyle
# Written for the reddit/r/DailyProgrammer challenge #245

gggg_alphabet = ['g', 'G', 'gg', 'gG', 'Gg', 'GG', 'ggg', 'ggG' 'gGg',
                'gGG', 'Ggg', 'GgG', 'GGg' 'GGG', 'gggg', 'gggG',
                'ggGg', 'ggGG', 'gGgg', 'gGgG', 'gGGg', 'gGGG', 'Gggg',
                'GggG', 'GgGg', 'GgGG']

def create_dictionary(text):
    translator = {}
    for letter in text:
        if not letter.isalpha():
            continue
        if translator.get(letter) == None:
            translator[letter] = gggg_alphabet[get_letter(letter)]
    return translator

def get_letter(character):
    if character.isupper():
        return ord(character) - 65
    else:
        return ord(character) - 97


def translate_to_gggg(text, dictionary):
    translation = ''
    for letter in text:
        if not letter.isalpha():
            translation += letter
        if (dictionary.get(letter)) != None:
            translation += dictionary.get(letter)
    return translation

def print_dict(dictionary):
    for k,v in dictionary.items():
        print(k + ' ' + v + ' ', end="")
    print()


message = input('Enter a message: ')
gg_dict = create_dictionary(message)
gg_translation = translate_to_gggg(message, gg_dict)
print_dict(gg_dict)
print(gg_translation)
