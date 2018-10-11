# -*- coding: utf-8 -*-

__author__ = 'Len Dierickx'
__email__ = 'len@astuanax.com'
__version__ = '0.1.2'


import os
import json

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
LANGUAGE_DIR = os.path.join(CURRENT_DIR, 'languages')
STOPWORDS_CACHE = {}

with open(os.path.join(LANGUAGE_DIR, 'languages.json'), 'rb') as mapping:
    res = mapping.read()
    res = res.decode('ascii')
    LANGUAGE_MAPPING = json.loads(res)

AVAILABLE_LANGUAGES = list(LANGUAGE_MAPPING.values())


class LanguageNotAvailable(Exception):
    pass


def get_stopwords(language, cache=True):
    try:
        language = LANGUAGE_MAPPING[language]
    except KeyError:
        if language not in AVAILABLE_LANGUAGES:
            raise LanguageNotAvailable('{0}" language is unavailable.'.format(
                language
            ))

    if cache and language in STOPWORDS_CACHE:
        return STOPWORDS_CACHE[language]

    language_filename = os.path.join(LANGUAGE_DIR, language + '/default.txt')
    try:
        with open(language_filename, 'rb') as language_file:
            stopwords = [line.decode('utf-8').strip()
                         for line in language_file.readlines()]
    except IOError:
        raise LanguageNotAvailable(
            '{0}" file is unreadable, check your installation.'.format(
                language_filename
            )
        )

    if cache:
        STOPWORDS_CACHE[language] = stopwords

    return stopwords


def clean(txt_list, stopwords_language, safe=True):
    if safe:
        stopwords_set = set(safe_get_stopwords(stopwords_language))
    else:
        stopwords_set = set(get_stopwords(stopwords_language))
    for sw in stopwords_set.intersection(txt_list):
        while sw in txt_list:
            txt_list.remove(sw)
    return txt_list


def safe_get_stopwords(stopwords_language):
    """
    :type stopwords_language: basestring
    :rtype: list
    """
    try:
        return get_stopwords(stopwords_language)
    except LanguageNotAvailable:
        return []


def languages():
    return AVAILABLE_LANGUAGES;

def print_languages():
    for lang in AVAILABLE_LANGUAGES:
        print lang
