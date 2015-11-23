#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import os.path
import pathlib
import re


DICT_PATH = pathlib.Path(os.path.expanduser('~/.vim/spell/'))
SPELL_REGEX = re.compile(r'[^\.]*')


def read_words(dict_path):
    word_set = set()
    with dict_path.open() as dictionary:
        for word in dictionary:
            word_set.add(word[:-1])
    return word_set


def write_words(dict_path, word_set):
    with dict_path.open('w') as dictionary:
        for word in sorted(word_set):
            dictionary.write(word+'\n')


def get_path(name):
    return DICT_PATH.joinpath(name)


def print_stats(old_words, new_words, merged_words):
    frm_str = '{:^7} {:^7} {:^7}'
    header_str = frm_str.format('old', 'new', 'merged')
    out_str = frm_str.format(len(old_words), len(new_words), len(merged_words))
    print(header_str)
    print(out_str)


def choose_dictionary():
    files = [child.name for child in DICT_PATH.iterdir() if SPELL_REGEX.fullmatch(child.name)]
    for n, f in enumerate(files):
        print('{:>} {}'.format(n, f))
    choice = int(input(':'))
    return files[choice]


def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--choose', action='store_true')
    args, rest = parser.parse_known_args()
    if args.choose:
        rest.insert(0, choose_dictionary())

    parser.add_argument('dictionary', help='dictionary file')
    parser.add_argument('words', nargs='*', help='words that will be added')
    args = parser.parse_args(rest)
    path = get_path(args.dictionary)
    old_words = read_words(path)
    new_words = set(args.words)
    merged_words = old_words | new_words
    write_words(path, merged_words)
    print_stats(old_words, new_words, merged_words)


if __name__ == "__main__":
    main()
