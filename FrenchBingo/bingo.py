# -*- coding: latin-1 -*-

import codecs
import collections
import itertools
import unicodedata


def remove_accent(word):
	'''
	Return the words sans accents
	ex. étudier -> etudier
	'''
	return ''.join(c for c in unicodedata.normalize('NFD', word) if unicodedata.category(c) != 'Mn')


def read_file(filename, encoding='utf-8'):
	with codecs.open(filename, 'r', encoding) as f:
		with_accents = (line.strip() for line in f.readlines())

	d = collections.defaultdict(list)
	for word in with_accents:
		d[remove_accent(word)].append(word)
	return d 


def find_words(word_list, letters, sort_by_length=False):
	possibilities = set() 
	for length in range(0, len(letters) + 1):
		possibilities |= set(''.join(p) for p in itertools.permutations(letters, length))

	valid_keys = list(word_list.keys() & possibilities)
	results = [word for key in valid_keys for word in word_list[key]] 

	if sort_by_length:
		results.sort(key=len, reverse=True) 

	return(results)
