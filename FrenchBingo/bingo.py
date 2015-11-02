# -*- coding: latin-1 -*-

import codecs
import collections
import itertools

from unicodedata import normalize, category


def remove_accent(word):
    '''
    Return the words sans accents
    ex. étudier -> etudier
    '''
    return ''.join(c for c in normalize('NFD', word) if category(c) != 'Mn')


def read_file(filename, encoding='utf-8'):
    with codecs.open(filename, 'r', encoding) as f:
        with_accents = (line.strip() for line in f.readlines())

    d = collections.defaultdict(set)
    for word in with_accents:
        d[remove_accent(word)].add(word)
    return d


def find_words(word_list, letters, sort_by_length=False):
    valid_keys = []
    for length in range(0, len(letters) + 1):
        for p in itertools.permutations(letters, length):
            word = ''.join(p)
            if word in word_list:
                valid_keys.append(word)

    results = list(set(word for key in valid_keys for word in word_list[key]))

    if sort_by_length:
        results.sort(key=len, reverse=True)

    return(results)
