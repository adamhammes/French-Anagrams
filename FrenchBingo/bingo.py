import codecs
import itertools
import unicodedata


def remove_accent(word):
        ''' Return the words sans accents
        ex. étudier -> etudier'''
        return ''.join(c for c in unicodedata.normalize('NFD', word) if unicodedata.category(c) != 'Mn')


def read_file(filename, encoding='utf-8'):
        with codecs.open(filename, 'r', encoding) as f:
                with_accents = [line.strip() for line in f.readlines()]

        no_accents = (remove_accent(word) for word in with_accents)
        return frozenset(word for word in no_accents)


def find_words(word_list, letters, sort_by_length=False):
        possibilities = set() 
        for length in range(0, len(letters) + 1):
                possibilities |= set([''.join(p) for p in itertools.permutations(letters, length)])

        results = list(word_list & possibilities)
        if sort_by_length:
                results.sort(key=len, reverse=True) 

        return(results)
