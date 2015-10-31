import codecs
import itertools
import unicodedata


def remove_accent(word):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')


def read_file(filename, encoding='utf-8', max_word_length=10):
    with codecs.open(filename, 'r', encoding) as f:
        raw_lines = f.readlines()
        
    no_accents = [remove_accent(line) for line in raw_lines]
    return frozenset([word for word in no_accents if len(word) <= max_word_length]) 
    

def find_words(word_list, letters):
    return word_list & set(itertools.permutations(letters))
