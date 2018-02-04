# -*- encoding: utf-8 -*-
# !/usr/bin/env python3
"""
Accepts the path to a text file and extracts the words from it, without repetition,
and writs them to a text file 'unique_words_list.txt' in the samedirectory/folder.
"""
import string
from pathlib import Path


def extract_words(text, replacee_chars, replacer_chars):
	for replacee in replacee_chars:
		for replacer in replacer_chars:
			text = text.replace(replacee, replacer)
	text = text.replace(',', ' ')
	text = text.replace('\n', ' ')
	text = set(text.split())
	text = set(word.split("'")[0] for word in text)
	return text

def get_symbols_to_be_replaced(text, symbols_to_be_kept):
	symbols = set(string.whitespace).union(string.punctuation).difference(symbols_to_be_kept)
	chars_in_text = set(text)
	not_printable_chars = set(char_ for char_ in chars_in_text if char_ not in string.printable)
	symbols_to_remove = chars_in_text.intersection(symbols)
	symbols_to_remove = symbols_to_remove.union(not_printable_chars)
	return symbols_to_remove


def make_path(raw_path):
	for char_ in ["'", '"', ' ']:
		raw_path = raw_path.strip(char_)
	filepath = Path(raw_path).expanduser()
	return filepath
	
def main():
	symbols_to_be_kept = [" ", "'"]
	filepath = input('Enter the path to the text (*.txt) file from which words are to be extracted:')
	filepath = make_path(raw_path=filepath)
	text = filepath.read_text(errors='replace')
	symbols_to_be_replaced = get_symbols_to_be_replaced(text, symbols_to_be_kept)
	text = extract_words(text, replacee_chars=symbols_to_be_replaced, replacer_chars=[' '])
	output_file = Path(filepath.with_name('unique_words_list.txt'))
	output_file.write_text('\n'.join(sorted(text)))
	print(f'Word list saved: {output_file}')
	

if __name__ == '__main__':
	main()
