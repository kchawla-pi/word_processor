# -*- encoding: utf-8 -*-
# !/usr/bin/env python3
"""
Accepts the path to a text file and extracts the words from it, without repetition,
and writs them to a text file 'unique_words_list.txt' in the samedirectory/folder.
"""
import string
import sys
from pathlib import Path


def read_second():
	pass
	

def get_text(filepath):
	filepath = Path(filepath).expanduser()
	try:
		with open('C:/Users/kshit/OneDrive/Desktop/test_word_dedup.txt', 'rb') as f:
			text_byte = f.read()
	# text = filepath.read_text()
	except FileNotFoundError as excep_in:
		cwd_filepath = Path.cwd().joinpath(filepath.name)
		# text = cwd_filepath.read_text(errors='ignore')
	except:
		raise
	else:
		text = [charac for charac in text_byte if str(charac).isalnum() or str(charac) in (' ', "'") ]
		text = [chr(charac) for charac in text]
		return ''.join(text)
	
	
def extract_words(text):
	text = text.lower()
	symbols = set(string.punctuation).difference(text)
	symbols.update({'\n', '\t'})
	symbols.discard("'")
	for symbol_ in symbols:
		text = text.replace(symbol_, ' ')
	text = set(text.split())
	text = set(word.split("'")[0] for word in text)
	return text


def make_messages(filepath):
	msgs = {
		'.': (f'\nCould not find the file "{filepath.name}" in the current directory/folder.\n'
		      f'Make sure the file exists and there are no typing errors.\n'
		      ),
		'path': (
			f'\nCould not find the file "{filepath.name}" in "{filepath.parent}" or in the current directory/folder.\n'
			f'Make sure the path and the file exist and there are no typing errors.\n'
			),
		'read': f'Successsfully read the file {filepath.name}',
		'write': f'Successsfully created the file at {Path.cwd()}',
		'write_err': f'You do not appear to have permission to write in the current lcoation.\nFile has been created at {Path.home()}',
		}
	return msgs


def read_file(filepath, msgs):
	try:
		text = get_text(filepath)
	except FileNotFoundError as excep:
		msg_ = msgs.get(str(filepath.parent), msgs['path'])
		print(msg_)
		sys.exit()
	else:
		words = extract_words(text)
		print(msgs['read'])
		return words
	
	
def write_wordslist(text, filename, filepath, msgs):
	try:
		Path(filepath.with_name(filename)).write_text('\n'.join(sorted(text)))
	except PermissionError:
		msgs.get('write_err')
	else:
		print(msgs.get('write'))
	
	
def main():
	wordslist_filename = 'unique_words_list.txt'
	filepath = 'C:/Users/kshit/OneDrive/Desktop/test_word_dedup.txt'
	filepath = Path(filepath)
	# filepath = Path(input('Enter the complete path to the text (*.txt) file from which words are to be extracted: ')).expanduser()
	msgs = make_messages(filepath)
	text = read_file(filepath, msgs)
	write_wordslist(text, wordslist_filename, filepath, msgs)


if __name__ == '__main__':
	main()
	quit()
	r"""
	C:\Users\kshit\OneDrive\Desktop\test_word_dedup.txt
	'C:/Users/kshit/OneDrive/Desktop/test_word_dedup.txt'
	"""
	with open('C:/Users/kshit/OneDrive/Desktop/test_word_dedup.txt', 'rb') as f:
		text_byte = f.read()
		# for line in f:
		# 	print(line.decode())
	text = text_byte.decode()
	print(text)
